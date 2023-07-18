from functools import cmp_to_key

n = int(input())

ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, a + b))

indices = list(range(n))

def compare(i, j):
    ai, aj = ab[i]
    bi, bj = ab[j]
    return (ai * bj < aj * bi) - (ai * bj > aj * bi)

sorted_indices = sorted(indices, key=cmp_to_key(compare))

for i in sorted_indices:
    print(i + 1, end=' ')
