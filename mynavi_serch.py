import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

# python 未経験で検索
url = 'https://tenshoku.mynavi.jp/list/kwpython_kw%E6%9C%AA%E7%B5%8C%E9%A8%93/?jobsearchType=14&searchType=18'
request = requests.get(url)

soup = BeautifulSoup(request.content, "html.parser")
# div_tag = soup.select('.container__inner')

# 会社名
name_list = []
names = soup.select('.cassetteRecruit__name')  
for name in names: 
    name_list.append(name.text.split('|')[0])  #会社名以降を削除

# URL
url_list = []
urls = soup.find_all('a', class_='js__ga--setCookieOccName')
for url in urls: 
    url_list.append('http://tenshoku.mynavi.jp' + url.attrs['href'].split('/?ty')[0]) #href抽出、url_listに書き込み、http~の追加、/?ty以降の削除
    url_list = (list(dict.fromkeys(url_list))) #重複を削除  
        
# 仕事内容
detail_list = []
details = soup.select('div > div.cassetteRecruit__detail > div.cassetteRecruit__main > table > tbody > tr:nth-child(1) > td')
for detail in details: 
    detail_list.append(detail.text)

# 対象者
target_list = []
targets = soup.select('div > div.cassetteRecruit__detail > div.cassetteRecruit__main > table > tbody > tr:nth-child(2) > td')
for target in targets: 
    target_list.append(target.text)

# 勤務地
location_list = []
locations = soup.select('div > div.cassetteRecruit__detail > div.cassetteRecruit__main > table > tbody > tr:nth-child(3) > td')
for location in locations: 
    location_list.append(location.text)

# 給与
salary_list = []
salarys = soup.select('div > div.cassetteRecruit__detail > div.cassetteRecruit__main > table > tbody > tr:nth-child(4) > td')
for salary in salarys: 
    salary_list.append(salary.text)

df_title_url = pd.DataFrame({'会社名':name_list,'URL':url_list,'仕事内容':detail_list,'対象者':target_list,'勤務地':location_list,'給与':salary_list})
print(df_title_url)
df_title_url.to_csv('mynavi_serch.csv',encoding='cp932', errors='ignore')