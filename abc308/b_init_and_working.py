N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))
sum = 0

for i in range(N):
    if C[i] in D:
        for j in range(len(D)):
            if C[i] == D[j]:
                sum += P[j+1]
    else:
        sum += P[0]

print(sum)
