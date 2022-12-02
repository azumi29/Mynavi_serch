from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager  

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
SERCH_WORD = 'python 未経験'
error_flg = False
target_url = 'https://tenshoku.mynavi.jp/'
driver.get(target_url)  
sleep(10)
print('動作確認')

try:
    sleep(20)
    # button = driver.find_element(By.CSS_SELECTOR,'#karte-3620180 > div.karte-widget__container > div > div > div._CloseButton__3xX2_ > button')
    # button = driver.find_element(By.XPATH,'//*[@id="karte-3620180"]/div[2]/div/div/div[1]/button')
    # button = driver.find_element(By.XPATH,'//*[@id="karte-3620180"]')
    button = driver.find_element(By.CLASS_NAME,'karte-close')
    # button = driver.find_element(By.CLASS_NAME,'_SurveyEditor_TemplateForms__3xX2_')

    # #アクティブレイヤーに切り替える　→　not clickable at point (563, 492)
    # elem = driver.switch_to.active_element
    # sleep(20)
    # button = elem.find_element(By.CLASS_NAME,'karte-close')

    sleep(20)
    button.click()

    sleep(10)

# except Exception:
#     error_flg = True
#     print('×ボタン押下時にエラーが発生しました。')
except Exception as e:
        print('content: ' + str(e))