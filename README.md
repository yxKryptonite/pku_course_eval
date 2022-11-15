# pku_course_eval
An automated program to submit course evaluation.

copyright (c) 2022 [@yxKryptonite](https://github.com/yxKryptonite)

**强烈要求教务部取消[评教新规](https://bbs.pku.edu.cn/v2/post-read.php?bid=438&threadid=18427237&page=5)！**

使用方法：
1. 克隆此仓库并进入目录
   ```bash
   git clone git@github.com:yxKryptonite/pku_course_eval.git
   cd pku_course_eval
   ```

2. 安装 python3 以及 `main.py` 中的依赖库
   ```bash
   pip install -r requirements.txt
   ```

3. 修改配置文件 `config.yaml` 中的 `username` 和 `password` 为你的学号和密码，修改 `eval_words` 为你想要评价的话（超过10个字）。

4. 运行 `main.py`，程序会自动提交评教
   ```bash
    python main.py
    ```

你也可以在本地使用浏览器进行互动式使用（无需修改 `config.yaml` ，但需要安装依赖库）：
```bash
streamlit run bot.py
```

目前暂无在线版本（等我解决Chrome的事情再说orz）...
