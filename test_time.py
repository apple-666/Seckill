import datetime
import time

# taobao_time = datetime.datetime.strptime(time1, '%H:%M:%S.%f')  # 字符串 变 date
taobao_time = datetime.datetime(2022, 10, 29, 22, 22, 10, 100000)
print('taobao_time:')
print(taobao_time)
print('\n')

while True:
    # now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    now = datetime.datetime.now()
    print(now)
    # time.sleep(5)
    if now > taobao_time:
        print('大于了')
        break
