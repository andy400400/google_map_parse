import requests
import json
from bs4 import BeautifulSoup 
import time
from urllib import parse
import re

def get_request(location):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    title_url = 'https://www.google.com.tw/maps/place/' + location
    html = requests.get(title_url, headers= headers) #將此頁面的HTML GET下來
    soup = BeautifulSoup(html.text,"html.parser") #將網頁資料以html.parser
    return soup

def parse_address(address):
    #URL編碼轉換
    address_str = parse.unquote(address[0])
    #取代前後/
    address_str = address_str.replace("/", "")
    # 去除地址前的郵遞區號
    split_list = re.split('^\d*', address_str,1)
    
    if(len(split_list) < 2):
        return ''
    else:
        return split_list[1]

def parse_request(soup):
    script = soup.select('script')
    str_script = str(script[8])
    split_by_url = str_script.split('https://www.google.com.tw/maps/preview/place')[1]
    split_by_sign = split_by_url.split('@')
    address = split_by_sign[0].split(',')
    location = split_by_sign[1].split(',')
    lat = location[0]
    lng = location[1]
    return address, lat, lng

tStart = time.time()#計時開始
location = '台北市中正區北平西路3號'
soup = get_request(location)
try:
    address_html, lat, lng  = parse_request(soup)
    address = parse_address(address_html)
    print(address,lat,lng)
except Exception as e:
    print(e)
    print('no data')

tEnd = time.time()#計時結束
print('time : ' + str(tEnd - tStart))#原型長這樣    
