n = 8
arr = [-1,2,4,-3,5,3,-6,2]

best = 0
for left in range(n):
    for right in range(n):
        sum = 0
        for k in range(left,right+1):
            sum += arr[k]
        best = max(sum,best)

print(best)