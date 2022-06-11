n = 8
arr = [-1,2,4,-3,5,3,-6,2]

best = 0
for left in range(n):
    sum = 0
    for mover in range(left,n):
        sum += arr[mover]
        best = max(sum,best)

print(best)