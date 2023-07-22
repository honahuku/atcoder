# https://atcoder.jp/contests/abc300/tasks/abc300_b
import logging

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
    output = "No"

    for h in range(H):
        new_array = A
        for _ in range(h):
            new_array = vertical(new_array, H, W)
        for w in range(W):
            logging.debug(f"(h, w): ({h}, {w})")
            for _ in range(w):
                new_array = horizontal(new_array, H, W, B)
                # for line in new_array:
                #     logging.debug("".join(line))
            # for line in new_array:
            #     logging.debug("".join(line))
            logging.debug(A)
            logging.debug(new_array)
            logging.debug(B)
            if new_array == B:
                output = "Yes"
    print(output)


# たて
def vertical(array, H, W):
    new_array = [[""] * int(W) for _ in range(int(H))]
    for offset in range(1, H + 1):
        # logging.debug("---")

        base = offset - 1
        if offset > H - 1:
            offset -= H

        # logging.debug(f"base={base}, offset={offset}")
        new_array[base] = array[offset]

        # logging.debug("array")
        # for line in array:
        # logging.debug("".join(line))
        # logging.debug("new_array")

        # num = 0
        # for line in new_array:
        #     logging.debug(f"{num}, {''.join(line)}")
        #     num += 1

    return new_array


# よこ
def horizontal(array, H, W, B):
    new_array = [[""] * int(W) for _ in range(int(H))]
    for offset in range(W):
        # logging.debug("---")

        base = offset - 1
        if offset > H - 1:
            offset -= H

        # logging.debug(f"base={base}, offset={offset}")
        for i in range(H):
            # logging.debug(f"i={i}")
            new_array[i][base] = array[i][offset]
            if new_array == B:
                logging.debug(f"{i},{base}")
        # logging.debug(f"{new_array}")

    return new_array


if __name__ == "__main__":
    main()
