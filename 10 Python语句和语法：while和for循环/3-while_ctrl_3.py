import time
import signal
import sys


def sigint_handler(signum, frame):  # 定义处理方法
    print("接收到管理员的ctrl+c!")
    print("退出程序")
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)
# 定义了收到’ctl+c’（SIGINT）这个信号后的处理方法为sigint_handler
while True:
    time.sleep(2)
    print('请输入Ctrl + C来停止这个循环')
