# https://atcoder.jp/contests/abc186/tasks/abc186_a
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

# logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    N, W = map(int, input().split())

    # 切り捨て除算
    ans = N // W
    print(ans)


if __name__ == "__main__":
    main()
