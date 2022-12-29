<div align=center><img src="assets/icon.png" height=150></div>
<h1 align=center>北大课程评估自动化</h1>

> 消极自由，即是免于他人干涉的自由。
> <p align="right">——伊努曼尔·康德</p>

<!-- **强烈要求教务部取消[评教新规](https://bbs.pku.edu.cn/v2/post-read.php?bid=438&threadid=18427237)！捍卫我们的「消极自由」！** -->

<!-- ## Online Demo

[网页链接](https://pku-course-evaluation-bot.streamlit.app)（本网页不会保存和泄漏您的学号和密码，请放心食用！） -->

## 使用方法：
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
   - `browser`: 你所使用的浏览器（首字母大写，目前支持 Chrome, Firefox, Edge 和 Safari 浏览器）

4. 运行 `main.py`，程序会自动提交评教
   ```bash
    python main.py
    ```

你也可以在本地使用浏览器进行图形化操作（无需修改 `config.yaml` ，但需要安装依赖库）：
```bash
streamlit run bot.py
```
<!-- 或使用上述的 [Online Demo](https://github.com/yxKryptonite/pku_course_eval#online-demo) 进行操作。 -->

<!-- ## Notes:

- 在线版本已发布，但该服务器较为脆弱，可能无法承受大量流量，所以还是推荐本地使用（本地也可以使用图形化界面）。
- 期末评估代码已经发布，如遇 bug ，请在 [issue](https://github.com/yxKryptonite/pku_course_eval/issues) 中提出。
- 如果 [Online Demo](https://github.com/yxKryptonite/pku_course_eval#online-demo) 挂了，请立刻在 [issue](https://github.com/yxKryptonite/pku_course_eval/issues) 中提出，作者会 reboot 服务器。 -->

## License

[GPL-3.0](LICENSE)

copyright (c) 2022 <a href="https://github.com/yxKryptonite">@yxKryptonite</a>
