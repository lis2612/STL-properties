from bs4 import BeautifulSoup
import requests

def parse():
    URL='https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/'
    HEADERS={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    response=requests.get(URL,headers=HEADERS)
    soup=BeautifulSoup(response.content,'html.parser')
    items=soup.findAll('div',class_='offer-wrapper')
    comps=[]

    for item in items:
        comps.append({
            'title':item.find('a',class_='marginright5 link linkWithHash detailsLink linkWithHashPromoted').get_text(strip=True)
        })
        for comp in comps:
            print(comp['title'])
    

parse()
