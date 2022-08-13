import pandas as pd
import openpyxl
import requests
from bs4 import BeautifulSoup
import json
import time

df = pd.read_excel('eetgroup/keyboards.xlsx')
mpn_list = list(df['mpn'])

ean_list = []
name_list = []

def get_wid(mpn, name_list):
    
    url = "https://api.eetgroup.com/api/Search/Search"

    querystring = {"term":mpn,"page":"1","pageSize":"30","showScore":"false","explain":"false","useFlattenedCategoryTree":"true","isExternalProductGuide":"false","showInStockFilter":"true"}

    headers = {
        "cookie": "ARRAffinity=79216fecd1b1d89ce691c4ba394369c1e00b1b6d27986ec3740b26e5827dc9c8; ARRAffinitySameSite=79216fecd1b1d89ce691c4ba394369c1e00b1b6d27986ec3740b26e5827dc9c8",
        "authority": "api.eetgroup.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
        "content-type": "application/json",
        "origin": "https://www.eetgroup.com",
        "referer": "https://www.eetgroup.com/",
        "sec-ch-ua": "^\^.Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "x-eet-businessentityid": "11",
        "x-eet-culture": "en-eu",
        "x-eet-localkey": "00b7745e-d370-4bfe-a9d1-4a230dbfc068",
        "x-eet-marketid": "1016",
        "x-eet-sessionkey": "818c65d3-ae8a-4aa9-b057-3577a004a5b9",
        "x-eet-siteid": "50"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    j = json.loads(response.text)
    try:
        product = j['model']['products'][0]
        display_name = product['displayName']
        wid = product['wid']
    except:
        wid = ''
        display_name = ''
    name_list.append(display_name)
    print(mpn, display_name, wid)
    return wid, name_list


def get_ean(wid, ean_list):

    url = "https://api.eetgroup.com/api/Product/details"

    querystring = {"productWid":wid}

    headers = {
        "cookie": "ARRAffinity=79216fecd1b1d89ce691c4ba394369c1e00b1b6d27986ec3740b26e5827dc9c8; ARRAffinitySameSite=79216fecd1b1d89ce691c4ba394369c1e00b1b6d27986ec3740b26e5827dc9c8",
        "authority": "api.eetgroup.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
        "content-type": "application/json",
        "origin": "https://www.eetgroup.com",
        "referer": "https://www.eetgroup.com/",
        "sec-ch-ua": "^\^.Not/A",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "x-eet-businessentityid": "11",
        "x-eet-culture": "en-eu",
        "x-eet-localkey": "00b7745e-d370-4bfe-a9d1-4a230dbfc068",
        "x-eet-marketid": "1016",
        "x-eet-sessionkey": "818c65d3-ae8a-4aa9-b057-3577a004a5b9",
        "x-eet-siteid": "50"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    js = json.loads(response.text)
    try:
        ean = js['model']['ean']
        ean_list.append(ean)
        
    except:
        ean_list.append('')
        
    print(ean)
    return ean_list


for each in mpn_list[:10]:
    wid, name_list = get_wid(each, name_list)
    if wid == '':
        ean_list.append("")
    else:
        ean_list = get_ean(wid, ean_list)

ean_list += ['' for i in range(2053-len(ean_list))]
name_list += ['' for i in range(2053-len(name_list))]

l = [2 for i in range(20)]
l += (['' for i in range(2053-len(l))])

df['ean'] = ean_list
df['model'] = name_list


df.to_csv('eetgroup/denemekeyborad.csv', index=False)