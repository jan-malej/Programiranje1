import orodja
import re
import os
import requests

IME_DATOTEKE = 'raw_html.txt' 
PATH = 'Datoteke'
URL ='https://www.tripadvisor.com/RestaurantSearch-g35805-oa00-Chicago_Illinois.html#EATERY_LIST_CONTENTS'

def spl_stran_v_string(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:  
        print('Ni povezave.')
        return None
    if r.status_code == requests.codes.ok:
        return r.text
    else:
        print('Napaka.')
        return None

def string_to_datoteka(niz):
    os.makedirs(PATH, exist_ok=True)
    path = os.path.join(PATH, IME_DATOTEKE)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(niz)
    return None

def shrani_stran():
    niz = spl_stran_v_string(URL)
    string_to_datoteka(niz)
    return None

shrani_stran()




# nato z regexi ločimo na bloke - restavracije
# nato z regexi prefiltriram vsak blok
# dobljeno zapišemo v csv