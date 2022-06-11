n = 8
arr = [-1,2,4,-3,5,3,-6,2]

best = 0
sum = 0
for right in range(n):
    sum = max(arr[right], sum+arr[right])
    best = max(best,sum)

print(best)