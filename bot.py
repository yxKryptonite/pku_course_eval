'''PKU课程评估Bot——本地版'''
from utils import login, get_link_list, daily_feedback, final_evaluation
import streamlit as st


st.set_page_config(
    page_title="PKU课程评估Bot",
    page_icon="assets/icon.png",
    layout="centered",
    menu_items={
        'About': "**强烈要求教务部取消[评教新规](https://bbs.pku.edu.cn/v2/post-read.php?bid=438&threadid=18427237&page=5)！捍卫我们的「消极自由」！**",
        'Report a bug': "https://github.com/yxKryptonite/pku_course_eval/issues",
        'Get Help': "https://github.com/yxKryptonite/pku_course_eval#readme"
    }
)


if __name__ == "__main__":
    st.title("PKU课程评估Bot——本地版")
    eval_data = {}
    eval_data['username']   = st.text_input("请输入学号")
    eval_data['password']   = st.text_input("请输入密码", type="password")
    eval_data['eval_words'] = st.text_area("请输入评估内容")
    eval_data['browser']    = st.selectbox("请选择浏览器", ["Chrome", "Firefox", "Edge", "Safari"])
    choice = st.radio("请选择评估类型", ("日常反馈", "期末评估"), index=1)

    if st.button("开始评估"):
        with st.spinner("正在登录..."):
            driver = login(eval_data, browser=eval_data['browser'])

        with st.spinner("正在获取链接..."):
            fb, ev = get_link_list(driver)

        with st.spinner("正在评估..."):
            if choice == "日常反馈":
                for link in fb:
                    daily_feedback(driver, link, eval_data)
                    
            elif choice == "期末评估":
                for link in ev:
                    final_evaluation(driver, link, eval_data)

        driver.close()
        st.success("自动评教已完成！")
