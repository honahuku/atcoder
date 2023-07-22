# https://atcoder.jp/contests/abc311/tasks/abc311_b
import logging

# logging.basicConfig(format="%(message)s", level=logging.DEBUG)


def main():
    N, D = map(int, input().split())
    S = []
    for _ in range(N):
        A = input()
        S.append(A)
    logging.debug(f"N: {N}, S: {S}")
    sanka = []

    for i in range(D):
        hitorimae = True
        logging.debug(f"hitorimae: {hitorimae}")
        for j in range(N):
            # logging.debug(f"i: {i}, j: {j}, S[j][i]: {S[j][i]}")
            if S[j][i] == "o" and hitorimae is True:
                logging.debug(f"hit! i: {i}, j: {j}, S[j][i]: {S[j][i]}")
                if j == (N - 1):
                    sanka.append(1)
                    logging.debug(f"sanka: {sanka}")
                    break
            elif S[j][i] == "x":
                hitorimae = False
                logging.debug(f"hitorimae: {hitorimae}")
                # if j == (N - 1):
                sanka.append(0)
                logging.debug(f"sanka: {sanka}")
                break

    print(max_consecutive_ones(sanka))

def max_consecutive_ones(lst):
    count = 0
    result = 0
    for num in lst:
        if num == 1:
            count += 1
            result = max(result, count)
        else:
            count = 0
    return result

if __name__ == "__main__":
    main()
