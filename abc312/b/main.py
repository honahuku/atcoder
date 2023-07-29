import logging
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    N, M = map(int, input().split())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    # logging.debug(f"{N}, {M}, {S}")

    pat1 = "###."
    pat2 = "...."
    pat3 = ".###"

    for i in range(N):
        if i + 8 > N:
            break
        for j in range(M):
            if j + 8 > M:
                break
            # logging.debug(f"{i}, {j}")

            if (
                S[i][j : j + 4] == pat1
                and S[i + 1][j : j + 4] == pat1
                and S[i + 2][j : j + 4] == pat1
            ):
                if S[i + 3][j : j + 4] == pat2 and S[i + 5][j + 5 : j + 9] == pat2:
                    if (
                        S[i + 6][j + 5 : j + 9] == pat3
                        and S[i + 7][j + 5 : j + 9] == pat3
                        and S[i + 8][j + 5 : j + 9] == pat3
                    ):
                        print(i + 1, j + 1)


if __name__ == "__main__":
    main()
