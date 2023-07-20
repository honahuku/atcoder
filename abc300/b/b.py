# https://atcoder.jp/contests/abc300/tasks/abc300_b

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# たて
def vertical (array):
    new_arry = [[''] * int(W) for _ in range(int(H))]
    print(array)
    print(new_arry)
    for i in range(H):
        if i <= H-1:
            logging.debug(i)
            logging.debug(array[i])
            print(i, ((i+1)%(H-1)), ((i+2)%(H-1)))
            new_arry[i][i], new_arry[((i+1)%(H-1))][i] = array[((i+1)%(H-1))][i], array[((i+2)%(H-1))][i]
            
            # iが0の時からnew_arryに値が入っていない？
            logging.debug(new_arry[i])
    return new_arry

# # よこ
# def horizontal (array):
#     new_arry = [[''] * int(W) for _ in range(int(H))]
#     for i in range(H):
#         if i <= W:
#             logging.debug(i)
#             logging.debug(array[i])
#             logging.debug(new_arry[i])
#             new_arry[i][i], new_arry[i][(i+1)%W] = array[i][(i+1)%W], array[i][(i+2)%W]
#     return new_arry

H, W = map(int, input().split())
A = []
for i in range(H):
    array = list(input())
    A.append(array)

B = []
for i in range(H):
    array = list(input())
    B.append(array)

logging.debug('---')

new_A = A
for _ in range(1):
    new_A = vertical(new_A)

for l in new_A:
    logging.debug(''.join(l))
