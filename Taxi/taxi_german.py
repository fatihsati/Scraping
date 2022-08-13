import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_links():
    url = 'https://www.taxi-heute.de/de/adressen/kategorien/955'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    base_url = 'https://www.taxi-heute.de/'
    link_txt = open('links.txt','w', encoding='utf-8')


    items = soup.find_all('div', {'class':'adressen col-md-4 col-sm-6 col-12 views-row'})

    for item in items:

        link = item.find('div', {'class':'views-field views-field-title'}).find('a')['href']
        link = base_url+link
        link_txt.write(link+'\n')
        
        
    link_txt.close()
    

def get_taxi_infos():
    with open('links.txt', 'r', encoding='utf-8') as f:
        links = f.read().split('\n')[:-1]
        
    taxi_data = []
    
    for url in links:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        try:
            strasse = soup.find('div', {'class':'field field--name-field-adresse-strasse-nr field--type-string field--label-inline clearfix'}).text.strip().split('\n')[1]
        except AttributeError:
            strasse = ''
        print(strasse)
        try:
            ort = soup.find('div', {'class':'field field--name-field-adresse-plz-ort field--type-string field--label-inline clearfix'}).text.strip().split('\n')[1]
        except AttributeError:
            ort = ''
        print(ort)
        try:
            bundesland = soup.find('div', {'class':'field field--name-field-adressen-bundesland field--type-entity-reference field--label-inline clearfix'}).text.strip().split('\n')[1]
        except AttributeError:
            bundesland = ''
        print(bundesland)
        try:
            ansprechpartner = soup.find('div', {'class': 'field field--name-field-adresse-ansprechpartner field--type-string field--label-inline clearfix'}).text.strip().split('\n')[1]
        except AttributeError:
            ansprechpartner = ''
        print(ansprechpartner)
        try:
            telefon = soup.find('div', {'class': 'field field--name-field-adresse-telefon field--type-string field--label-above'}).text.strip().split('\n')[-1]
        except AttributeError:
            telefon = ''
        print(telefon)
        try:
            telefax = soup.find('div', {'class': 'field field--name-field-adresse-telefax field--type-string field--label-above'}).text.strip().split('\n')[-1]
        except AttributeError:
            telefax = ''
        print(telefax)
        try:
            mail = soup.find('div', {'class': 'field field--name-field-adresse-mail field--type-email field--label-above'}).text.strip().split('\n')[-1]
        except AttributeError: 
            mail = ''
        print(mail)
        try:
            link = soup.find('div', {'class': 'field field--name-field-adresse-link field--type-link field--label-above'}).text.strip().split('\n')[-1]
        except AttributeError:
            link = ''
        print(link)
        
        info = {'strasse': strasse,
                'PLZ, Ort': ort,
                'bundesland': bundesland,
                'ansprechpartner': ansprechpartner,
                'telefon': telefon,
                'telefax': telefax,
                'mail': mail,
                'link': link}
        
        taxi_data.append(info)
    
    df = pd.DataFrame(taxi_data)
    df.to_csv('taxi.csv', encoding='utf-8')
get_taxi_infos()
