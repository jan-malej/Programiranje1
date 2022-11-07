import orodja
import re

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

vzorec_imena = re.compile(
    r'"name":"(?P<ime>.+?)","average',
    flags=re.DOTALL
)

vzorec_ocene = re.compile(
    r'Rating":(?P<ocena>.*?),',
    flags=re.DOTALL
)

vzorec_st_glasov = re.compile(
    r'"userReviewCount":(?P<stevilo>\d*?),',
    flags=re.DOTALL
)

vzorec_price_tag = re.compile(
    r'"priceTag":"(?P<price_tag>.*?)",',
    flags=re.DOTALL
)

vzorec_types = re.compile(
    r'"establish.*?:\[(?P<tipi>.*?)\],',
    flags=re.DOTALL
)

vzorec_gumba = re.compile(
    r'"buttonText":"(?P<gumb>.*?)",',
    flags=re.DOTALL
)
# nato z regexi ločimo na bloke - restavracije
# nato z regexi prefiltriram vsak blok
# dobljeno zapišemo v csv

#orodja.shrani_spletno_stran(URL, IME_DATOTEKE, vsili_prenos=True)
#for url in generiraj_url_naslove(2):
    #orodja.shrani_spletno_stran(url, IME_DATOTEKE, vsili_prenos=True)