S = list(map(int, input().split()))
bool = "No"

for i in range(len(S)):
    if (i > 0):
        if (S[i] > S[i-1]) and S[i] >= 100 and S[i] <= 675 and S[i]%25 == 0 and bool == "Yes":
            bool = "Yes"
        else:
            bool = "No"
    elif S[i]%25 == 0:
        bool = "Yes"

print(bool)
