import logging
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

# logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    logging.debug(f"{N},{M},{A},{B}")
    A_sorted = sorted(A)
    B_sorted = sorted(B, reverse=True)
    logging.debug(f"{N},{M},{A_sorted},{B_sorted}")

    for i in range(A_sorted[0], B_sorted[0] + 1):
        sellers = sum(x <= i for x in A_sorted)
        buyers = sum(x >= i for x in B_sorted)
        if buyers <= sellers:
            print(i)
            return

    print(B_sorted[0] + 1)


if __name__ == "__main__":
    main()
