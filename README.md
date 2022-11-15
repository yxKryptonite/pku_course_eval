# pku_course_eval
An automated program to submit course evaluation.

copyright (c) 2022 [@yxKryptonite](https://github.com/yxKryptonite)

**强烈要求教务部取消[评教新规](https://bbs.pku.edu.cn/v2/post-read.php?bid=438&threadid=18427237&page=5)！**

使用方法：
1. 安装 python3 以及 `main.py` 中的依赖库
   ```bash
   pip install -r requirements.txt
   ```

2. 修改配置文件 `config.yaml` 中的 `username` 和 `password` 为你的学号和密码，修改 `eval_words` 为你想要评价的话（超过10个字）。

3. 运行 `main.py`，程序会自动提交评教
   ```bash
    python main.py
    ```

你也可以使用网页端进行互动式使用（无需修改 `config.yaml` ，但需要安装依赖库）：
```bash
streamlit run app.py
```

网页在线版本正在开发中...
