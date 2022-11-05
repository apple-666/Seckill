import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pykeyboard import *

# 全自动化Python代码操作
# v2版：selenium+request
# 步骤：
# 1, selenium 实现登录，定位到产品页面，选择产品参数，点击下单
# 2, request 对订单进行付款

# py3.8 使用方式
s = Service('C:/Program Files/Google/Chrome/Application/chromedriver')
browser = webdriver.Chrome(service=s)


# py3.7 使用方式
# browser = webdriver.Chrome()
# chrome=R"C:/Program Files/Google/Chrome/Application/chromedriverexe"
# browser = webdriver.Chrome(chrome)

def login():
    browser.get(
        "https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z02.1.972272805.d4919660.7BUp5h&action=itemlist/BoughtQueryAction&event_submit_do_query=1&tabCode=waitPay")

    # btn_login_value = '亲，请登录'
    # btn_login = WebDriverWait(browser, 10, poll_frequency=0.1).until(EC.presence_of_element_located(
    #     (By.LINK_TEXT, btn_login_value)))
    # btn_login.click()

    btn_saoma_xpath = '//*[@id="login"]/div[1]/i'
    btn_saoma = WebDriverWait(browser, 60, poll_frequency=0.1).until(EC.presence_of_element_located(
        (By.XPATH, btn_saoma_xpath)))
    btn_saoma.click()

    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def del_order():
    # 取消订单：
    pre_count = 0
    while True:
        dis_one_xpath = '//*[@id="cancelOrder"]'
        dis_all = browser.find_elements(by=By.XPATH, value=dis_one_xpath)
        print(len(dis_all))
        if len(dis_all) != pre_count:
            pre_count = len(dis_all)
            dis_one = WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located(
                (By.XPATH, dis_one_xpath)))
            dis_one.click()

            # other_xpath = '//*[@id="tp-bought-root"]/div[1]/div[1]/div[3]/span[1]/span[1]'
            # other = WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located(
            #     (By.XPATH, other_xpath)))
            # other.click()
            #
            # ret_xpath = '//*[@id="tp-bought-root"]/div[1]/div[1]/div[2]/span[1]/span[1]'
            # ret = WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located(
            #     (By.XPATH, ret_xpath)))
            # ret.click()
        else:
            time.sleep(0.5)

    # 下拉框
    # selector_xpath = '//*[@id="J_CloseReason"]'
    # selector = WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located(
    #     (By.XPATH, selector_xpath)))
    # selector.click()

    # 下拉框 选一个
    # sel_one_xpath = '//*[@id="J_CloseReason"]/option[2]'
    # sel_one = WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located(
    #     (By.XPATH, sel_one_xpath)))
    # sel_one.click()

    # 确定
    # confirm_xpath = '//*[@id="J_CancelOrderForm"]/div[5]/button'
    # confirm = WebDriverWait(browser, 10, 0.1).until(EC.presence_of_element_located(
    #     (By.XPATH, confirm_xpath)))
    # confirm.click()
    return 1


if __name__ == "__main__":
    login()
    del_order()
