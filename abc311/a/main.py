# https://atcoder.jp/contests/abc311/tasks/abc311_a
import logging

# logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    N = int(input())
    S = input()
    A = False
    B = False
    C = False
    logging.debug(f"N: {N}, S: {S}")

    for i in range(len(S)):
        if S[i] == "A":
            A = True
        elif S[i] == "B":
            B = True
        elif S[i] == "C":
            C = True
        if A == True and B == True and C == True:
            print(i+1)
            exit()
        logging.debug(f"i: {S[i]}")


if __name__ == "__main__":
    main()
