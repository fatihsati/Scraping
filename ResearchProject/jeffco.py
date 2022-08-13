import requests
from bs4 import BeautifulSoup
from google_drive_downloader import GoogleDriveDownloader as gdd


url = 'https://www.jeffcopublicschools.org/services/facilities/lead_tests'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

def download_pdf(link, file_index):
    
    id = link.split('=')[1]
    gdd.download_file_from_google_drive(file_id=id,
                                    dest_path=f'ResearchProject/file{file_index}.pdf',
                                    unzip=False)



page = soup.find('div', {'id':'ctl00_ContentPlaceHolder1_ctl11_divContent'})
li_list = page.find_all('li')

index = 0
for each in li_list:
    link = each.find('a')['href']
    download_pdf(link, index)
    index +=1




