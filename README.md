# pku_course_eval
An automated program to submit course evaluation.

copyright (c) 2022 [@yxKryptonite](https://github.com/yxKryptonite)

“自由人，就是不受阻碍地做他想做的事情的人。” ——霍布斯《利维坦》

**强烈要求教务部取消[评教新规](https://bbs.pku.edu.cn/v2/post-read.php?bid=438&threadid=18427237&page=5)！捍卫我们的消极自由！**

[Online Demo](https://pku-course-evaluation-bot.streamlit.app)（本网页不会保存和泄漏您的学号和密码，请放心食用！）

使用方法：
1. 克隆此仓库并进入目录
   ```bash
   git clone git@github.com:yxKryptonite/pku_course_eval.git
   cd pku_course_eval
   ```

2. 安装 python3 及本项目依赖库
   ```bash
   pip install -r requirements.txt
   ```

3. 修改配置文件 `config.yaml`
   - `username`: 你的学号
   - `password`: 你的密码
   - `eval_words`: 你想要评价的话（超过10个字）
   - `browser`: 你所使用的浏览器（首字母大写，目前支持 Chrome, Firefox, Edge 和 Safari）

4. 运行 `main.py`，程序会自动提交评教
   ```bash
    python main.py
    ```

你也可以在本地使用浏览器进行图形化操作（无需修改 `config.yaml` ，但需要安装依赖库）：
```bash
streamlit run bot.py
```
或使用上述的 [Online Demo](https://pku-course-evaluation-bot.streamlit.app) 进行操作。

## FAQ:

- 在线版本已发布，但该服务器较为脆弱，可能无法承受大量流量，所以还是推荐本地使用（本地也可以使用图形化界面）。
- 由于期末评估尚未开放，所以本项目是用日常反馈进行测试的。待期末评估开放后，作者会 commit 最新代码。
- 如果 [Online Demo](https://pku-course-evaluation-bot.streamlit.app) 挂了，请立刻在 [issue](https://github.com/yxKryptonite/pku_course_eval/issues) 中提出，作者会 reboot 服务器。
