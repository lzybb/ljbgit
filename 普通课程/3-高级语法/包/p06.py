import sys

if __name__ == '__main__':
    print(type(sys.path))
    # print(sys.path)
    for p in sys.path:
        print(p)
