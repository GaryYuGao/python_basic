def sys_argv(a, b):
    print(int(a) + int(b))


if __name__ == '__main__':
    # sys_argv(5, 6)
    import sys
    # print(sys.argv[0])
    sys_argv(sys.argv[1], sys.argv[2])
    # # # sys_argv(1, 2)
