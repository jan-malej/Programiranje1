import orodja
import re
import os
import requests

IME_DATOTEKE = 'raw_html2.txt' 
PATH = 'Datoteke'
URL ='https://www.tripadvisor.com/RestaurantSearch-g35805-oa00-Chicago_Illinois.html#EATERY_LIST_CONTENTS'

def sestavi_url(n):
    n *= 3
    url = f'https://www.tripadvisor.com/RestaurantSearch-g35805-oa{n}0-Chicago_Illinois.html#EATERY_LIST_CONTENTS'
    return url

def generiraj_url_naslove(n):
    for i in range(n):
        yield sestavi_url(i)

#orodja.shrani_spletno_stran(URL, IME_DATOTEKE, vsili_prenos=True)
for url in generiraj_url_naslove(2):
    orodja.shrani_spletno_stran(url, IME_DATOTEKE, vsili_prenos=True)





# nato z regexi ločimo na bloke - restavracije
# nato z regexi prefiltriram vsak blok
# dobljeno zapišemo v csv