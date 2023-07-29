import logging
import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    S = input()
    l = ["ACE","BDF","CEG","DFA","EGB","FAC","GBD"]
    if S in l:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
