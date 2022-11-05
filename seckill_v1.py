import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 全自动化Python代码操作
# v1版：受网速影响，没法在1s内实现下单+付款

s = Service('C:/Program Files/Google/Chrome/Application/chromedriver')
browser = webdriver.Chrome(service=s)


def login(auto_type):
    browser.get("https://www.taobao.com")
    time.sleep(2)  # 点击
    if browser.find_element(by=By.LINK_TEXT, value='亲，请登录'):
        browser.find_element(by=By.LINK_TEXT, value='亲，请登录').click()
        time.sleep(10)
        # 打开购物车列表首页
        browser.get("https://cart.taobao.com/cart.htm")
        time.sleep(2)
    # 勾选 购物车所有宝贝
    # if browser.find_element(by=By.ID, value='J_SelectAll1'):
    #     browser.find_element(by=By.ID, value='J_SelectAll1').click()

    # 勾选第一个宝贝
    # 用xpath：//*[@id="J_Item_2967515444920"]/ul/li[1]/div/div/div/label
    #           //*[@id="J_Item_2965409928843"]/ul/li[1]/div/div/div/label
    #           //*[@id="J_Item_2968102611224"]/ul/li[1]/div/div/div/label
    item_xpath_val = '//*[@id="J_Item_2968418214643"]/ul/li[1]/div/div/div/label'
    while True:
        if browser.find_element(by=By.XPATH, value=item_xpath_val):
            browser.find_element(by=By.XPATH, value=item_xpath_val).click()
            break
        time.sleep(0.1)

    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def item():
    browser.get(
        "https://detail.tmall.com/item.htm?id=683976756890&sku_properties=10004:7195672376;122216431:27772&spm=a1z0d.6639537/tb.1997196601.22.3d387484sFjLwK")


def order(times):
    while True:
        # 记录当前时间，使用datatime内置模块
        now = datetime.datetime.now().strftime("%H:%M:%S.%f")
        print(times)
        print(now)
        # 对比时间，时间到的话就点击结算
        # if now == times:
        try:
            if browser.find_element(by=By.ID, value='J_Go'):
                browser.find_element(by=By.ID, value='J_Go').click()
                browser.find_element(by=By.LINK_TEXT, value='提交订单').click()
                print('抢购成功，请尽快付款')
                break
        except:
            print('请再次尝试提交订单')
        # print(now)
        time.sleep(0.2)


# 输入密码自动付钱
def buy():
    # 提交订单
    # //*[@id="submitOrderPC_1"]/div[1]/a[2]
    # while True:
    #     if browser.find_element(by=By.XPATH, value='//*[@id="submitOrderPC_1"]/div[1]/a[2]'):
    #         browser.find_element(by=By.XPATH, value='//*[@id="submitOrderPC_1"]/div[1]/a[2]').click()
    #         break
    #     time.sleep(0.1)

    # 输入密码
    #  //*[@id="payPassword_rsainput"]
    while True:
        if browser.find_element(by=By.XPATH, value='//*[@id="payPassword_rsainput"]'):
            input_ps = browser.find_element(by=By.XPATH, value='//*[@id="payPassword_rsainput"]')
            input_ps.click()
            input_ps.send_keys(123456)
            break
        print('输入密码的框')
        time.sleep(0.1)
    return 0


if __name__ == "__main__":
    login(1)
    # item()
    # 微秒
    order('00:35:00.200000')
    buy()
