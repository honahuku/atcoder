import logging
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    D = int(input())
    ans = D / 100
    print(ans)


if __name__ == "__main__":
    main()
