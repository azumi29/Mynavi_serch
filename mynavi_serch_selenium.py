from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
SERCH_WORD = 'python 未経験'
driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver_win32 (5)/chromedriver.exe')
error_flg = False
target_url = 'https://tenshoku.mynavi.jp/'
driver.get(target_url)  
sleep(10)
print('動作確認')

try:
    sleep(30)
    # login_button = driver.find_element(By.CSS_SELECTOR,'#karte-3620180 > div.karte-widget__container > div > div > div._CloseButton__3xX2_ > button')
    # login_button = driver.find_element(By.XPATH,'//*[@id="karte-3620180"]/div[2]/div/div/div[1]/button')
    login_button = driver.find_element(By.CLASS_NAME,'_SurveyEditor_TemplateForms__3xX2_')
    sleep(20)
    login_button.click()
    sleep(10)
# except Exception:
#     error_flg = True
#     print('×ボタン押下時にエラーが発生しました。')
except Exception as e:
        print('content: ' + str(e))