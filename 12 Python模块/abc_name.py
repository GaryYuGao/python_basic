print("import run this")

def get_device_info(ip):
    # 工具函数：供其他模块导入调用
    return {"ip": ip, "status": "online"}

# 入口判断：只有直接运行 abc.py 时才执行下面的测试代码
if __name__ == '__main__':
    # 本地测试代码
    print(get_device_info("192.168.1.1"))
