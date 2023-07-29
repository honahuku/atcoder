# https://atcoder.jp/contests/abc214/tasks/abc214_a

import logging
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

# logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    N = int(input())
    if N <= 125:
        print(4)
    elif N <= 211:
        print(6)
    elif N <= 214:
        print(8)
    else:
        logging.critical("N is out of range")


if __name__ == "__main__":
    main()
