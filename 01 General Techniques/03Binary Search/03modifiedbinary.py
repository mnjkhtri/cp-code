n = 11
arr = [1,4,-5,12,-1,-2,41,18,31,9,11]
arr.sort()
print(arr)

tosearch = 19
def imp_func(element):
    return element <= tosearch

current = 0
gap = n//2
while gap >= 1:
    while current+gap < n and imp_func(arr[current+gap]):
        current += gap
    gap //= 2

if arr[current]==tosearch:
    print("found at",current)
else:
    print("not found")


