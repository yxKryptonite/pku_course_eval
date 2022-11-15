from main import login, get_link_list, daily_feedback, final_evaluation
import streamlit as st
from selenium import webdriver
import yaml
import time

if __name__ == "__main__":
    st.title("PKU课程评估Bot")
    eval_data = {}
    eval_data['username']   = st.text_input("请输入学号")
    eval_data['password']   = st.text_input("请输入密码", type="password")
    eval_data['eval_words'] = st.text_area("请输入评估内容")

    if st.button("开始评估"):
        driver = login(eval_data)
        link_list = get_link_list(driver)
        for link in link_list:
            daily_feedback(driver, link, eval_data)

        st.success("自动评教已完成！")
        st.balloons()
