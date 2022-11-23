from utils import login, get_link_list, daily_feedback, final_evaluation
import yaml


if __name__ == "__main__":
    with open('config.yaml', 'r', encoding="UTF-8") as f:
        eval_data = yaml.load(f, Loader=yaml.FullLoader)

    driver = login(eval_data, browser=eval_data['browser'])
    fb, ev = get_link_list(driver)
    # print(link_list)

    # 通过链接进入评估页面，这里先用日常反馈测试
    # for link in fb:
    #     daily_feedback(driver, link, eval_data)

    for link in ev:
        final_evaluation(driver, link, eval_data)

    driver.close()
    print("自动评教已完成！")