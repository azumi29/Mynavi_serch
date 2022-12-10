from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager  
from bs4 import BeautifulSoup
import pandas as pd
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
SERCH_WORD = 'python 未経験'
error_flg = False
target_url = 'https://tenshoku.mynavi.jp/'
driver.get(target_url)  
sleep(3)
print('動作確認')

# アンケート画面の「×」ボタンクリック
try:
    sleep(3)
    button = driver.find_element(By.CLASS_NAME,'_sw-Btn__3xX2_.__support__3xX2_.__middle__3xX2_.karte-close')
    sleep(3)
    button.click()
    sleep(3)

except Exception:
    error_flg = True
    print('×ボタン押下時にエラーが発生しました。')

# Cookieを～画面の「閉じる」ボタンクリック
try:
    sleep(3)
    button02 = driver.find_element(By.CLASS_NAME,'_karte-temp-btn-close__2u7Y_.karte-close._karte-temp-hover__2u7Y_')
    sleep(3)
    button02.click()
    sleep(3)

except Exception:
    error_flg = True
    print('×ボタン押下時にエラーが発生しました。')

# 検索画面に入力
if error_flg is False:
    try:
        serch_word_input = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[2]/div/form/div[1]/input')
        serch_word_input.send_keys(SERCH_WORD)
        sleep(1)
 
        serch_word_input.submit()
        sleep(10)
        
    except Exception as e:
        print('検索キーワード入力時にエラーが発生しました。')
        # print(str(e))
        # error_flg = True


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

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
df_mynavi.to_csv('mynavi_serch.csv',encoding='cp932', errors='ignore')