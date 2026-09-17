import time

while True:
    try:  # 尝试去执行
        time.sleep(2)
        print('请输入Ctrl + C来停止这个循环')
    except KeyboardInterrupt:
        # 如果出现KeyboardInterrupt异常的处理方法
        print("接收到管理员的ctrl+c!")
        print("退出程序")
        break
