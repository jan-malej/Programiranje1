import orodja
import re
import os
import csv

IME_DATOTEKE = 'raw_html.txt' 
PATH = 'Datoteke'
URL ='https://www.tripadvisor.com/RestaurantSearch-g35805-oa00-Chicago_Illinois.html#EATERY_LIST_CONTENTS'

def sestavi_url(n):
    n *= 3
    url = f'https://www.tripadvisor.com/RestaurantSearch-g35805-oa{n}0-Chicago_Illinois.html#EATERY_LIST_CONTENTS'
    return url

vzorec_bloka = re.compile(
    r'\{"detailPageUrl.*?d\d+.+?"isStoryboardPublished"',
    flags=re.DOTALL   
)

vzorec_rest = re.compile(
    r'"name":"(?P<ime>.+?)".*?'
    r'averageRating":(?P<ocena>.*?),.*?'
    r'"userReviewCount":(?P<stevilo>\d*?),.*?'
    r'"priceTag":"(?P<price_tag>.*?)",.*?'
    r'"establish.*?:\[(?P<tipi>.*?)\],.*?'
    r'"buttonText":"(?P<gumb>.*?)",',
    flags=re.DOTALL
)

def podatki_iz_bloka(blok):
    restavracija = vzorec_rest.search(blok).groupdict()
    restavracija['ime'] = restavracija['ime']
    restavracija['ocena'] = restavracija['ocena']
    restavracija['st_ocen'] = restavracija['stevilo']
    restavracija['cenovni_razpon'] = restavracija['price_tag']
    restavracija['tipi'] = restavracija['tipi'].strip().split(', ')
    return restavracija

def ena_stran():
    vsebina = orodja.vsebina_datoteke(IME_DATOTEKE)
    for blok in vzorec_bloka.finditer(vsebina):
        yield podatki_iz_bloka(blok.group(0))

#restavracije = []
#for r in ena_stran():
#    restavracije.append(r)

#orodja.zapisi_json(restavracije, 'podatki/rest.json')
#orodja.zapisi_csv(restavracije, ['ime', 'ocena', 'st_ocen', 'cenovi_razpon', 'tipi'],'podatki/rest.csv')

# nato z regexi ločimo na bloke - restavracije
# nato z regexi prefiltriram vsak blok
# dobljeno zapišemo v csv

#orodja.shrani_spletno_stran(URL, IME_DATOTEKE, vsili_prenos=True)
#for url in generiraj_url_naslove(2):
    #orodja.shrani_spletno_stran(url, IME_DATOTEKE, vsili_prenos=True)


def v_bloke(vsebina):
    reg = re.compile(
    r'\{"detailPageUrl.*?d\d+'
    r'.+?"isStoryboardPublished"',
    flags=re.DOTALL
    )
    bloki = re.findall(reg, vsebina)
    return bloki

def iz_bloka_v_slovar(blok):
    reg = re.compile(
    r'"name":"(?P<ime>.+?)".*?'
    r'averageRating":(?P<ocena>.*?),.*?'
    r'"userReviewCount":(?P<stevilo>\d*?),.*?'
    r'"priceTag":"(?P<price_tag>.*?)",.*?'
    r'"establish.*?:\[(?P<tipi>.*?)\],.*?'
    r'"buttonText":"(?P<gumb>.*?)",',
    flags=re.DOTALL
    )
    data = re.search(reg, blok)
    slovar = data.groupdict()
    return slovar

def vse_restavracije():
    dat = orodja.vsebina_datoteke(IME_DATOTEKE)
    bloki = v_bloke(dat)
    rest = [iz_bloka_v_slovar(blok) for blok in bloki]
    return rest

def write_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None

def write_cat_ads_to_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
    slovarjev parametra ads enaki in je seznam ads neprazen."""
    # Stavek assert preveri da zahteva velja
    # Če drži se program normalno izvaja, drugače pa sproži napako
    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
    # produkcijskem okolju
    assert ads and (all(j.keys() == ads[0].keys() for j in ads))
    write_csv(ads[0].keys(), ads, directory, filename)

def main(redownload=True, reparse=True):
    vsebina = orodja.vsebina_datoteke(IME_DATOTEKE)
    rest = v_bloke(vsebina)
    rest_lepse = [iz_bloka_v_slovar(blok) for blok in rest]
    write_cat_ads_to_csv(rest_lepse, 'podatki', 'rest.csv')

if __name__ == '__main__':
    main() 