import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup as BS
from DRT import DRT
from db import save_DRT, get_all_drts

def get_DRTs(party_name='sha', schemaname=18): 
    '''
        using session, first I am fetching the captcha 
        and then using the fetched captcha, I am fetching the details 
        and then saving in sqlite3 db

    '''
    
    session = requests.Session()
    # response = session.get("https://drt.gov.in/front/page1_advocate.php")

    # saving captcha image
    response = session.get("https://drt.gov.in/front/captcha.php")
    file = open("captcha.png", "wb")
    file.write(response.content)
    file.close()

    # getting captcha from the captcha image saved
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = Image.open('captcha.png')
    captcha_text = pytesseract.image_to_string(im)
    # print(captcha_text)

    # getting details based on party_name, schemaname and the captcha
    payload = {
        'schemaname': schemaname,
        'name': party_name,
        'answer': int(captcha_text),
        'submit11': 'Search'
    }
    response = session.post("https://drt.gov.in/front/page1_advocate.php", data=payload)

    # using beautifulsoup, extracting the details rowwise from the table
    soup = BS(response.text, features="html.parser")
    rows = soup.find_all('table')[1].find('tbody').find_all('tr')

    drts = []
    for row in rows:
        cols = row.find_all("td")
        drts.append(DRT(cols[0].get_text(), cols[1].get_text(), cols[2].get_text(), cols[3].get_text(), 
                    cols[4].get_text(), cols[5].get_text(), cols[6].get_text(), cols[7].get_text()))

    return drts

if __name__ == "__main__":
    drts = get_DRTs(party_name='sha')
    for drt in drts:
        save_DRT(drt)
    print(get_all_drts())
