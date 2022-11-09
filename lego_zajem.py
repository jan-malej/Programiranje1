import orodja
import re

URL = 'https://www.lego.com/en-gb/categories/all-sets?page=2'
IME_DATOTEKE = 'nov_html.txt'
IME_CSV = 'Datoteke/podatki.csv'

def sestavi_url(n):
    """Generira url naslov v odvisnosti od n"""
    url = f'https://www.lego.com/en-gb/categories/all-sets?page={n}'
    return url

def sestavi_ime_datoteke(n):
    """Generira ime datoteke"""
    ime = f'Datoteke/lego_html_stran{n}.txt'
    return ime    

def iz_vsebine_v_bloke(vsebina):
    """Iz vsebine vrne seznam blokov"""
    vzorec_bloka = re.compile(
        r'\{"__typename":"SingleVariantProduct"'
        r'.*?__typename":"Price"\},',
        flags=re.DOTALL)
    bloki = re.findall(vzorec_bloka, vsebina)
    return bloki

def iz_bloka_v_slovar(blok):
    """Iz bloka vrne slovar iskanih podatkov"""
    vzorec_podatkov = re.compile(
        r'Single.*?"id":"(?P<id>\d+)".*?'
        r'"name":"(?P<ime>.*?)".*?'
        r'rating":(?P<ocena>.*?),.*?'
        r'canAddToBag":(?P<zaloga>.*?),.*?'
        r'centAmount":(?P<cena>\d*)',
        flags=re.DOTALL
    )
    podatki = re.search(vzorec_podatkov, blok)
    slovar = podatki.groupdict()
    return slovar

def vsi_izdelki_na_eni_strani(n):
    """Iz n-te strani vrne seznam slovarjev"""
    url = sestavi_url(n)
    ime_datoteke = sestavi_ime_datoteke(n)
    orodja.shrani_spletno_stran(url, ime_datoteke, headers={'Accept-Language': 'en'})
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    bloki = iz_vsebine_v_bloke(vsebina)
    out = [iz_bloka_v_slovar(blok) for blok in bloki]
    return out

def zapisi_csv(sez, polja, ime_datoteke):
    """Napiše csv datoteko iz seznama slovarjev, seznama imen polj"""
    orodja.zapisi_csv(sez, polja, ime_datoteke)
    print('Napisano!')

izdelki = []
polja = ['id', 'ime', 'ocena', 'zaloga', 'cena']
for st in range(2, 71):
    for izdelek in vsi_izdelki_na_eni_strani(st):
        izdelki.append(izdelek)

izdelki.sort(key=lambda izdelek: izdelek['id'])
zapisi_csv(izdelki, polja, IME_CSV)

