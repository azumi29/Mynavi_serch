from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager  #ここまでの4行はあってる

# from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver_win32 (5)/chromedriver.exe')
SERCH_WORD = 'python 未経験'
error_flg = False
target_url = 'https://tenshoku.mynavi.jp/'
driver.get(target_url)  
sleep(10)
print('動作確認')

# try:
#     sleep(20)
#     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # driver.execute_script("window.scrollTo(0,  " & button.Location.Y & ");")

#     # login_button = driver.find_element(By.CSS_SELECTOR,'#karte-3620180 > div.karte-widget__container > div > div > div._CloseButton__3xX2_ > button')
#     # login_button = driver.find_element(By.XPATH,'//*[@id="karte-3620180"]/div[2]/div/div/div[1]/button')
#     # login_button = driver.find_element(By.XPATH,'//*[@id="karte-3620180"]')
#     button = driver.find_element(By.CLASS_NAME,'karte-close')
#     # login_button = driver.find_element(By.CLASS_NAME,'_SurveyEditor_TemplateForms__3xX2_')

#     # driver.execute_script("arguments[0].click();", login_button)
#     # driver.execute_script('arguments[0].click();', login_button)

#     sleep(20)
#     # login_button.submit()
#     button.click()
#     sleep(10)

# # except Exception:
# #     error_flg = True
# #     print('×ボタン押下時にエラーが発生しました。')
# except Exception as e:
#         print('content: ' + str(e))


# #       
# # try:アラートは発生しませんでした
# #   wait = WebDriverWait(driver, 30)
# #   wait.until(EC.alert_is_present())
# #   alert = driver.switch_to.alert
# #   print(alert.text)
# # #   alert.accept()
# # except TimeoutException:
# #     print("アラートは発生しませんでした")
# # except Exception as e:
# #   print(e)