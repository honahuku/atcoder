s = input() 
x = ''.join(sorted(s))
for i in range(len(x)):
    if x[i] == x[i+1]:
        print('no')
        exit()

print(x[0])
