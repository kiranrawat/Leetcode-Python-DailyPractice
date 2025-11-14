arr = [-2, -3, -4, -100, 1, 2, 3, 4, 4]
# [-100, -4, -3, -2, 1, 2, 3, 4, 4]
arr.sort()
start = 0
end = len(arr)-1
print(start, end)
res = []

while start < end:
    total = arr[start] + arr[end]
    if total == 0:
        res.append([arr[start], arr[end]])
        # start += 1
        end -= 1
    elif (total > 0):
        end -= 1
    else:
        start += 1
print(res)
