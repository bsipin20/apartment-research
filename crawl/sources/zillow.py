import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import socket


from bs4 import BeautifulSoup

from crawl import helpers

url = "https://streeteasy.com/2-bedroom-apartments-for-rent/brooklyn"

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache',
    }

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
HOST = 'localhost'
PORT = 9009

def parse_page(r, socket):
    soup = BeautifulSoup(r.content, 'html.parser')
    #create the first two dataframes
    df = pd.DataFrame()
    postings = []
    for i in soup:
        address = soup.find_all(class_= 'list-card-addr')
        price = list(soup.find_all(class_='list-card-price'))
        beds = list(soup.find_all("ul", class_="list-card-details"))
        details = soup.find_all('div', {'class': 'list-card-details'})
        home_type = soup.find_all('div', {'class': 'list-card-footer'})
        last_updated = soup.find_all('div', {'class': 'list-card-top'})
        brokerage = list(soup.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
        link = soup.find_all(class_= 'list-card-link')

        for index, addr in enumerate(address):
            addr_ = address[index].contents[0]
            price_ = price[index].contents[0]
            last_updated_ = last_updated[index].contents[0].contents[0]
            link_ = link[index].contents[0]
            post = dict()
            post['address'] = addr_
            post['price'] = price_
            post['last_updated'] = last_updated_
            post['link'] = link_
            postings.append(post)
            socket.sendall(('trades,name=ilp_stream_1 value=12.4\ntrades,name=ilp_stream_2 value=11.4\n').encode())

    return postings


#BED = "2-_beds"
#BROOKLYN = "brooklyn-new-york"

base = 'https://www.zillow.com/'
url = 'https://www.zillow.com/homes/Carroll-Gardens,-New-York,-NY_rb/'
globalurl = 'https://www.zillow.com/homes/Astoria,-New-York,-NY_rb/'
url = 'https://www.zillow.com/brooklyn-new-york-ny/rentals/2-_beds/'
url = 'https://www.zillow.com/bay-ridge-brooklyn-new-york-ny/rentals/2-_beds/'
url2 = 'https://www.zillow.com/bay-ridge-brooklyn-new-york-ny/rentals/2-_beds/2_p/'
url2 = 'https://www.zillow.com/bay-ridge-brooklyn-new-york-ny/rentals/2-_beds/3_p/'
url3 = 'https://www.zillow.com/gowanus-brooklyn-new-york-ny/rentals/2-_beds/'

#2_p

#def get_links(burough, bedrooms = "2", rentals: True):
#    url = base + burough
#    return url
    
def parse_pages():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    with requests.Session() as s:
        r = s.get(globalurl, headers=req_headers)
        results = parse_page(r, sock)
        print(results)

parse_pages()



