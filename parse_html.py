import requests
import json
from bs4 import BeautifulSoup 
import time

def get_request(location):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    title_url = 'https://www.google.com.tw/maps/place/' + location
    html = requests.get(title_url, headers= headers) #將此頁面的HTML GET下來
    soup = BeautifulSoup(html.text,"html.parser") #將網頁資料以html.parser
    return soup

tStart = time.time()#計時開始
location = '台北市中正區北平西路3號'
soup = get_request(location)
try:
    script = soup.select('script')
    str_script = str(script[8])
    split_a = str_script.split('https://www.google.com.tw/maps/preview/place')[1]
    split_b = split_a.split('@')
    split_c = split_b[1].split(',')
    print(split_c[0],split_c[1])
except Exception as e:
    print('no data')

tEnd = time.time()#計時結束
print('process time : ' + str(tEnd - tStart))
