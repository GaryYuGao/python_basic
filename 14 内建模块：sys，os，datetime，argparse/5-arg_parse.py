def qyt_argparse(host, filename, iface):
    print(host)
    print(filename)
    print(iface)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = "python arg_parse.py -t host -f filename -i interface"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-f", "--file", dest="filename", help="中文Write content to FILE", default='1.txt', type=str)
    parser.add_argument("-i", "--interface", dest="iface", help="中文Specify an interface", default=1, type=int)
    parser.add_argument("-t", "--host", dest="host", help="中文Specify an host", default='10.1.1.1', type=str)
    # parser.add_argument(nargs='*', dest="hosts", help="Specify some hosts", default='10.1.1.1 10.1.1.2', type=str)
    args = parser.parse_args()

    qyt_argparse(args.host, args.filename, args.iface)
    # qyt_argparse(args.hosts, args.filename, args.iface)
