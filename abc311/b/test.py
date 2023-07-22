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

lst = [0,1,1,1,1,1,0,1,1,1,1,0]

print(max_consecutive_ones(lst))
