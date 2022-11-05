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
    browser.get("https://www.taobao.com")
    time.sleep(2)  # 点击
    btn_login_value = '亲，请登录'
    btn_login = WebDriverWait(browser, 10, poll_frequency=0.1).until(EC.presence_of_element_located(
        (By.LINK_TEXT, btn_login_value)))
    btn_login.click()
    time.sleep(8)
    # if browser.find_element(by=By.LINK_TEXT, value='亲，请登录'):
    #     browser.find_element(by=By.LINK_TEXT, value='亲，请登录').click()
    #     time.sleep(10)
    # while True:
    #     if browser.find_element(by=By.XPATH, value=item_xpath_val):
    #         browser.find_element(by=By.XPATH, value=item_xpath_val).click()
    #         break
    #     time.sleep(0.1)

    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


# 宝贝页面
# 选择宝贝参数并下单

def item_0():
    # x40 gt
    browser.get(
        "https://detail.tmall.com/item.htm?id=683976756890&sku_properties=10004:7195672376;122216431:27772&spm=a1z0d.6639537/tb.1997196601.22.3d387484sFjLwK")

    time.sleep(2)
    phone_color = browser.find_element(by=By.XPATH,
                                       value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div/div[1]/div[1]/div/div[1]/div/img')
    phone_color.click()
    phone_vulume = browser.find_element(by=By.XPATH,
                                        value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div/div[1]/div[2]/div/div[1]/div/span')
    phone_vulume.click()
    phone_conf = browser.find_element(by=By.XPATH,
                                      value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div[2]/div[5]/div/div/div[1]/div[4]/div/div[1]/div/span')
    phone_conf.click()

    # 下单
    get_order = browser.find_element(by=By.XPATH,
                                     value='//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div[2]/div[6]/div[1]/button/span[2]')
    get_order.click()


# 测试item：饼干

def item_1(taobao_time):
    print_time('网页打开前 ')

    browser.get(
        "https://detail.tmall.com/item.htm?abbucket=6&id=645470187561&ns=1&spm=a230r.1.14.1.34da37edcZHyzD&skuId=4814388378459")

    print_time('扫码登录前 ')
    # 点击扫码登录 //*[@id="login"]/div[1]/i
    btn_saoma_xpath = '//*[@id="login"]/div[1]/i'
    btn_saoma = WebDriverWait(browser, 20, poll_frequency=0.1).until(EC.presence_of_element_located(
        (By.XPATH, btn_saoma_xpath)))
    btn_saoma.click()

    print_time('扫码登录后 ')

    # 立即购买//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div[2]/div[6]/div[1]/button[1]
    # type2: //*[@id="J_LinkBuy"]
    btn_buy_xpath_map = ['//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div[2]/div[6]/div[1]/button[1]',
                         '//*[@id="J_LinkBuy"]']
    # btn_buy_xpath = btn_buy_xpath_map[0]
    btn_buy = None
    while True:
        btn_buys = browser.find_elements(by=By.XPATH, value=btn_buy_xpath_map[0])
        if len(btn_buys) != 0:
            btn_buy = browser.find_element(by=By.XPATH, value=btn_buy_xpath_map[0])
            break
        else:
            btn_buys = browser.find_elements(by=By.XPATH, value=btn_buy_xpath_map[1])
            if len(btn_buys) != 0:
                btn_buy = browser.find_element(by=By.XPATH, value=btn_buy_xpath_map[1])
                break
            time.sleep(0.1)
    btn_buy.click()

    # 提交订单
    btn_order_xpath = '//*[@id="submitOrderPC_1"]/div/a'
    btn_order = WebDriverWait(browser, 20, poll_frequency=0.1).until(EC.presence_of_element_located(
        (By.XPATH, btn_order_xpath)))
    while True:
        now = datetime.datetime.now()
        if now > taobao_time:
            btn_order.click()
            break

    print_time('--------注意 提交订单')
    # time.sleep(10)

    # 输入密码 有安全控件，无法直接定位和输入密码
    # input //*[@id="payPassword_rsainput"]
    # span://*[@id="payPassword_container"]

    # btn_inpu6')t_xpath = '//*[@id="payPassword_rsainput"]'
    #     # btn_input = WebDriverWait(browser, 10, poll_frequency=0.1).until(EC.presence_of_element_located(
    #     #     (By.XPATH, btn_input_xpath)))
    #     # btn_input.click()
    #     # btn_input.send_keys('12345

    # 确定
    # 1,用xpath
    # btn_enter_xpath = '//*[@id="validateButton"]'
    # btn_enter = WebDriverWait(browser, 10, poll_frequency=0.1).until(EC.presence_of_element_located(
    #     (By.XPATH, btn_enter_xpath)))
    # btn_enter.click()
    # 2, 用id
    # btn_enter2_id = 'validateButton'
    # btn_enter2 = WebDriverWait(browser, 10, poll_frequency=0.1).until(EC.presence_of_element_located(
    #     (By.ID, btn_enter2_id)))
    # btn_enter2.click()

    print_time('开始进入支付页面1、 ')

    # xpath = '//*[@id="remain_block"]/div[1]'

    # 先定位：其他支付方式 -> tab5次到 输入框 -> tab2次 到 确认框
    # 银行 //*[@id="ch-530cda1b0dc698ad13355522b9c92d6e747f8a241ca45064fccfbe6e3b3444a4"]
    # 下拉选项 //*[@id="channels"]/div/div/button[1]
    btn_input_xpath = '//*[@id="ch-530cda1b0dc698ad13355522b9c92d6e747f8a241ca45064fccfbe6e3b3444a4"]'
    btn_input = WebDriverWait(browser, 20, poll_frequency=0.1).until(EC.presence_of_element_located(
        (By.XPATH, btn_input_xpath)))
    btn_input.click()

    print_time('完成打开支付页面 ')

    k = PyKeyboard()  # 键盘的实例k

    action = ActionChains(browser)
    for i in range(0, 5):
        action.send_keys(Keys.TAB).perform()  # 按下并释放Tab键
        time.sleep(0.1)

    print_time('tab跳了4-5次')

    # 密码框
    # action.send_keys('123456')

    # 输入密码
    k.type_string('512729')
    # input_pwd(k, '123456')

    print_time('输入完密码')

    for i in range(0, 2):
        action.send_keys(Keys.TAB).perform()
    # 确认按钮
    action.send_keys(Keys.ENTER).perform()

    print_time('--------注意已付款 ')
    print('--------需要的时间是：' + str(taobao_time))


def print_time(msg):
    now_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
    print(msg + '时间为：' + now_time)


def to_item(itme_id):
    fun_name = "item_" + str(itme_id)
    # 跳到对应item的func
    globals()[fun_name]()


# 使用于购物车
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
    browser.get('https://www.taobao.com')
    # input_pwd2('apple')
    # login()
    # to_item(1)
    # taobao_time = datetime.datetime(2022, 10, 29, 22, 38, 3, 10000)
    # item_1(taobao_time)
    # 微秒
    # order('00:35:00.200000')
    # buy()
