N = int(input())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

pairs = [(a / (a + b), i) for i, (a, b) in enumerate(zip(A, B), 1)]

sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

for _, index in sorted_pairs:
    print(index, end=' ')
