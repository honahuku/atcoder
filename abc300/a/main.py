import sys

if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])

N, A, B = map(int, input().split())
C = list(map(int, input().split()))

print(C.index(A + B) + 1)
