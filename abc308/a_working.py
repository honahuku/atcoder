S = list(map(int, input().split()))
bool = "Yes"

for i in range(1, len(S)):
    if not (S[i] >= S[i-1] and S[i] >= 100 and S[i] <= 675 and S[i]%25 == 0):
        bool = "No"
        break

if not (S[0] >= 100 and S[0] <= 675 and S[0]%25 == 0):
    bool = "No"

print(bool)
