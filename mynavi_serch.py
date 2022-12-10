import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

# python 未経験で検索
url = 'https://tenshoku.mynavi.jp/list/kwpython_kw%E6%9C%AA%E7%B5%8C%E9%A8%93/?jobsearchType=14&searchType=18'
request = requests.get(url)

soup = BeautifulSoup(request.content, "html.parser")

name_list = []
url_list = []
detail_list = []
target_list = []
location_list = []
salary_list = []
for cassetteRecruit in soup.select('div[class="cassetteRecruit"]'):

    # 会社名
    names = cassetteRecruit.select_one('.cassetteRecruit__name' )
    for name in names: 
        name_list.append(name.text.split('|')[0])  #会社名以降を削除

    # URL
    urls = cassetteRecruit.select_one('.js__ga--setCookieOccName' )
    for url in urls: 
        url_list.append('http://tenshoku.mynavi.jp' + urls.attrs['href'].split('/?ty')[0]) #href抽出、url_listに書き込み、http~の追加、/?ty以降の削除

    # 仕事内容
    details = cassetteRecruit.select_one('table[class="tableCondition"] tr:nth-of-type(1) td')
    for detail in details: 
        detail_list.append(detail.text)

    # 対象者
    targets = cassetteRecruit.select_one('table[class="tableCondition"] tr:nth-of-type(2) td')
    for target in targets: 
        target_list.append(target.text)

    # 勤務地
    locations = cassetteRecruit.select_one('table[class="tableCondition"] tr:nth-of-type(3) td')
    for location in locations: 
        location_list.append(location.text)

    # 給与
    salaries = cassetteRecruit.select_one('table[class="tableCondition"] tr:nth-of-type(4) td')
    for salary in salaries: 
        salary_list.append(salary.text)

df_mynavi = pd.DataFrame({'会社名':name_list,'URL':url_list,'仕事内容':detail_list,'対象者':target_list,'勤務地':location_list,'給与':salary_list})
print(df_mynavi)
df_mynavi.to_csv('mynavi_serch08.csv',encoding='cp932', errors='ignore')