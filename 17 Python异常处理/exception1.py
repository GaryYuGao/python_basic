import re

def find_index(obj, index):
    print(obj[index])

if __name__ == '__main__':
    # find_index('qytang', 'cisco') # IndexError: string index out of range
    try:
        # find_index('qytang', 3)
        # find_index(10000, 1) # TypeError: 'int' object is not subscriptable
        # find_index('qytang', 'cisco') # TypeError: string indices must be integers, not 'str'
        find_index('qytang', 10) # IndexError: string index out of range
    except TypeError as e:
        print(f'TypeError: {e}')
        if re.match(r".*'int' object is not subscriptable", str(e)):
            print('整数对象是不支持索引的')
        elif re.match(r".*string indices must be integers", str(e)):
            print('索引必须是整数对象')
        else:
            print('其他索引错误', e)
    except IndexError as e:
        print('索引超出范围')
    except Exception as e:
        print(f'其他错误: {e}')
    else:
        print('没有任何错误发生！')
    finally:
        print('这个总是要打印的！')
