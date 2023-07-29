# https://atcoder.jp/contests/abc300/tasks/abc300_b
import logging
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        array = list(input())
        A.append(array)
    B = []
    for _ in range(H):
        array = list(input())
        B.append(array)

    # 組み合わせ(s,t)
    for s in range(H):
        for t in range(W):
            output = "Yes"
            # マス目(i,j)を全探索
            for i in range(H):
                for j in range(W):
                    logging.debug(
                        f"s={s} t={t} i={i} j={j} A={A[(i - s + H) % H][(j - t + W) % W]} B={B[i][j]}"
                    )
                    if A[(i - s + H) % H][(j - t + W) % W] != B[i][j]:
                        output = "No"
    print(output)


if __name__ == "__main__":
    main()
