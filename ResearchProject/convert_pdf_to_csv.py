
# from PyPDF2 import PdfReader

# r = PdfReader('ResearchProject/Jeffco_files/file0.pdf')
# file = r.pages[0].extract_text()
# print(type(file), file)


# first_row = file.split('\n')[1]
# print(first_row)



import requests

def download_pdf(link):
    
    id = link.split('id=')[1]
    print(id)

    download_url = f'https://drive.google.com/u/0/uc?id={id}&export=dowload'
    r = requests.get(download_url)
    # print(r.content)

download_pdf("https://drive.google.com/open?id=1I1DXKxUBRsxPMhVRTOrmfmzzg2GTxJ_9")










