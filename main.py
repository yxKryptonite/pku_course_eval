import requests
import re
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml


def login(eval_data, eval_url="http://kcpg.pku.edu.cn"):
    '''登录'''
    driver = webdriver.Chrome()
    driver.get(eval_url)
    time.sleep(3)
    # 登录，send_keys设置input框内容，click处理点击
    driver.find_element(By.XPATH, '//*[@id="user_name"]').send_keys(eval_data['username'])
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(eval_data['password'])
    driver.find_element(By.XPATH, '//*[@id="logon_button"]').click()
    time.sleep(3)
    return driver


def get_link_list(driver):
    '''获取课程评估链接列表'''
    container = driver.find_element(By.ID, "myTaskContainer")
    link_list = []
    feedbacks = container.find_elements(By.CLASS_NAME, "feedback")
    for feedback in feedbacks:
        link_list.append(feedback.get_attribute("href"))

    return link_list


def daily_feedback(driver, link, eval_data):
    '''日常反馈'''
    driver.get(link)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="topic"]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/textarea').send_keys(eval_data['eval_words'])
    driver.find_element(By.XPATH, '//*[@id="topic"]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[1]').click()


def final_evaluation(driver, link, eval_data):
    """
    * 期末评估 *
    评估有效认定：
    - 单门课程作答时间不少于2分钟
    - 填写开放性问题不少于10字
    - 所有评分指标选项不完全一致
    """
    driver.get(link)
    time.sleep(1)
    # TODO
    pass


if __name__ == "__main__":
    with open('kyx.yaml') as f:
        eval_data = yaml.load(f, Loader=yaml.FullLoader)

    driver = login(eval_data)
    link_list = get_link_list(driver)
    # print(link_list)

    # 通过链接进入评估页面，这里先用日常反馈测试
    for link in link_list:
        daily_feedback(driver, link, eval_data)

    driver.close()
    print("自动评教已完成！")