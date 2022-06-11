import sys
n = 8
arr = [1,3,2,5,1,1,2,3]

subsum = 0
required = 2
left = 0

minlength = sys.maxsize

thelist = []
for right in range(n):
    subsum += arr[right]
    while subsum >= required:

        if subsum == required:
            thelist.append((left,right))

        subsum -= arr[left]
        left += 1
print(thelist)



