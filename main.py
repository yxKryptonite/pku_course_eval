import requests
import re
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import yaml

with open('kyx.yaml') as f:
    eval_data = yaml.load(f, Loader=yaml.FullLoader)

eval_url = "http://kcpg.pku.edu.cn"

eval_words = eval_data['eval_words']

driver = webdriver.Chrome()
driver.get(eval_url)
time.sleep(3)
# send_keys设置input框内容  click处理点击
driver.find_element(By.XPATH, '//*[@id="user_name"]').send_keys(eval_data['username'])
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(eval_data['password'])
driver.find_element(By.XPATH, '//*[@id="logon_button"]').click()

time.sleep(3)
# 获取评估列表
container = driver.find_element(By.ID, "myTaskContainer")

# find the table
table = container.find_element(By.TAG_NAME, "table")
# find the second tbody
tbody = table.find_elements(By.TAG_NAME, "tbody")[1]
# find all tr
trs = tbody.find_elements(By.TAG_NAME, "tr")

link_list = []

for tr in trs:
    try:
        a = tr.find_element(By.TAG_NAME, "a")
    except:
        continue
    link = a.get_attribute("href")
    link_list.append(link)

# 进入评估页面，这里先用日常反馈测试
for link in link_list:
    driver.get(link)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="topic"]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/textarea').send_keys(eval_words)
    driver.find_element(By.XPATH, '//*[@id="topic"]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[1]').click()