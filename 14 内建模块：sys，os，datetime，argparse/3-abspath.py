import os

print(os.path.dirname(os.path.abspath(__file__)))

path = os.path.dirname(os.path.abspath(__file__))

def sys_argv(a, b):
    print(int(a) + int(b))
