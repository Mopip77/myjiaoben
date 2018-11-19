from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import win32api
import win32con
import time
import os


USERNAME = input('用户名:')
PWD = input('密码:')
classes_url = input('课件列表网址:')


chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
wait = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)

# 登陆
browser.get('https://bb.neu.edu.cn/webapps/login/')
input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#user_id'))
        )
pwd = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
        )
login_but = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#login > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type="image"]'))
        )
input.send_keys(USERNAME)
pwd.send_keys(PWD)
login_but.click()

# 登录状态下跳转到课程网站，找到每个课件超链接
browser.get(classes_url)
class_list = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.contentBox'))
        )
class_link = class_list.find_elements_by_tag_name('li')

# 下载，采用右键，按K另存为，按ENTER保存
i = 1
for link in class_link:
    vv = link.find_element_by_tag_name('a')
    ActionChains(browser).context_click(vv).perform()
    win32api.keybd_event(75,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)
    win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.5)
    print(i, vv.text)
    i += 1

print('[*]下载任务添加完成，下载完成后关闭浏览器')
