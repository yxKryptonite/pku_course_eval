import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
import random

SHORT_INTERVAL = 1
MID_INTERVAL   = 3
LONG_INTERVAL  = 5
GREAT_INTERVAL = 121 # > 2min


def login(eval_data, eval_url="http://kcpg.pku.edu.cn", browser="Chrome"):
    '''登录'''
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(options=opts)
    elif browser == "Edge":
        driver = webdriver.Edge()
    elif browser == "Safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Invalid browser name")

    driver.get(eval_url)
    time.sleep(LONG_INTERVAL)
    # 登录，send_keys设置input框内容，click处理点击
    driver.find_element(By.XPATH, '//*[@id="user_name"]').send_keys(eval_data['username'])
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(eval_data['password'])
    driver.find_element(By.XPATH, '//*[@id="logon_button"]').click()
    time.sleep(LONG_INTERVAL)
    return driver


def get_link_list(driver):
    '''
    返回值：两个列表

    `feedback_link_list`：日常反馈链接列表
    `evaluation_link_list`：课程评估链接列表
    '''
    time.sleep(SHORT_INTERVAL)
    container = driver.find_element(By.ID, "myTaskContainer")
    feedback_link_list = []
    evaluation_link_list = []
    try:
        feedbacks = container.find_elements(By.CLASS_NAME, "feedback")
        evaluations = container.find_elements(By.CLASS_NAME, "pingjia")
    except:
        raise ValueError("No such link")

    for feedback in feedbacks:
        feedback_link_list.append(feedback.get_attribute("href"))
    for evaluation in evaluations:
        evaluation_link_list.append(evaluation.get_attribute("href"))

    return feedback_link_list, evaluation_link_list


def daily_feedback(driver, link, eval_data):
    '''日常反馈'''
    driver.get(link)
    time.sleep(MID_INTERVAL)
    driver.find_element(By.XPATH, '//*[@id="topic"]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/textarea').send_keys(eval_data['eval_words'])
    driver.find_element(By.XPATH, '//*[@id="topic"]/div[2]/div/div[2]/div[1]/div[2]/div[2]/button[1]').click()


def final_evaluation(driver, link, eval_data):
    """
    期末评估

    评估有效认定：
    - 单门课程作答时间不少于2分钟
    - 填写开放性问题不少于10字
    - 所有评分指标选项不完全一致
    """
    driver.get(link)
    time.sleep(MID_INTERVAL)

    # ----------------- 内嵌函数 ----------------- #

    def page_wise(page):
        tab = page.find_element(By.CLASS_NAME, "tab-pane.active")
        try:
            selectives = tab.find_elements(By.CLASS_NAME, "question.SelectQ.clearfix.marginbt.radioFive")
            textareas = tab.find_elements(By.TAG_NAME, "textarea")
        except:
            raise ValueError("Invalid page")

        for question in selectives:
            choices = question.find_elements(By.CLASS_NAME, "radioFivelabel.backpo")
            if len(choices) == 0:
                choices = question.find_elements(By.CLASS_NAME, "checkboxFivelabel.cbxbackpo")

            rdn = random.randint(0, 4)
            choice = choices[rdn]
            choice.click()
            page.execute_script("arguments[0].scrollIntoView();", choice)

        for textarea in textareas:
            textarea.send_keys(eval_data['eval_words'])

    # ----------------- 内嵌函数 ----------------- #
        
    tabs = driver.find_element(By.CLASS_NAME, "tabOutside2.tabOutsideNew.tabOutside2New")
    ul = tabs.find_element(By.TAG_NAME, "ul")
    items = ul.find_elements(By.TAG_NAME, "li")

    for item in items:
        item.click()
        time.sleep(SHORT_INTERVAL)
        driver.execute_script("window.scrollTo(0, 0)")
        page_wise(driver)

    time.sleep(GREAT_INTERVAL)

    # submit
    submit_btn = driver.find_element(By.ID, "btnSave")
    driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
    submit_btn.click()
    time.sleep(SHORT_INTERVAL)
    confirm_btn = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
    driver.execute_script("arguments[0].scrollIntoView();", confirm_btn)
    confirm_btn.click()
    time.sleep(MID_INTERVAL)
