"""
@Name: main.py
@Auth: JiangZhesheng
@Date: 2022/9/12-18:54
@Desc: 武大进出校报备脚本，用selenium模拟登录，填表，提交
"""

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

url="https://hall.whu.edu.cn/infoplus/form/XSCRSQ/start"

username="2022202110006"
password="jzs981225"

info_address="圆梦美丽家园10-1-102"
info_reason='回家'
info_trans='586'
info_phone='15527786655'

# info_startdate='2022-09-09'
# info_enddate='2022-09-09'
info_startdate=time.strftime('%Y-%m-%d')
info_enddate=time.strftime('%Y-%m-%d')
info_starttime='01:00'
info_endtime='23:00'

chrome_options=Options()
# 浏览器后台运行
# chrome_options.add_argument('--headless')
browser=webdriver.Chrome(options=chrome_options)

browser.get(url)
browser.maximize_window()
browser.implicitly_wait(5)

tag_username=browser.find_element(By.XPATH,'//*[@id="username"]')
tag_username.clear()
tag_username.send_keys(username)

tag_password=browser.find_element(By.XPATH,'//*[@id="password"]')
tag_password.clear()
tag_password.send_keys(password)

tag_password.send_keys(Keys.ENTER)
time.sleep(3)
while True:
    if 'XSCRSQ' in browser.current_url:
        break
startbutton=browser.find_element(By.ID,'preview_start_button')
browser.execute_script('arguments[0].click()',startbutton)



while True:
    if 'form' in browser.current_url:
        time.sleep(2)
        break

phone=browser.find_element(By.ID,'V1_CTRL28')
address=browser.find_element(By.ID,'V1_CTRL53')
reason=browser.find_element(By.ID,'V1_CTRL9')
trans=browser.find_element(By.ID,'V1_CTRL10')
startdate=browser.find_element(By.ID,'V1_CTRL7')
starttime=browser.find_element(By.ID,'V1_CTRL22')
enddate=browser.find_element(By.ID,'V1_CTRL8')
endtime=browser.find_element(By.ID,'V1_CTRL23')


address.send_keys(info_address)
reason.send_keys(info_reason)
trans.send_keys(info_trans)

startdate.clear()
time.sleep(1)
startdate.send_keys(info_startdate)
starttime.clear()
time.sleep(1)
starttime.send_keys(info_starttime)

action=ActionChains(browser)
action.click(phone)
action.perform()
time.sleep(1)

enddate.clear()
time.sleep(1)
enddate.send_keys(info_enddate)
endtime.clear()
time.sleep(1)
endtime.send_keys(info_endtime)

counselor=browser.find_element(By.CLASS_NAME,'selection')
action=ActionChains(browser)
action.click(counselor)
action.perform()
time.sleep(1)
input=browser.find_element(By.CLASS_NAME,"select2-search__field")
input.send_keys("于雅梦")
input.send_keys(Keys.ENTER)

submit=browser.find_element(By.CLASS_NAME,'command_button_content')
browser.execute_script('arguments[0].click()',submit)

time.sleep(2)

browser.find_element(By.XPATH,'//*[@class="dialog display"]/div[2]/button[1]').click()
browser.find_element(By.XPATH,'//*[@class="dialog display"]/div[2]/button').click()
