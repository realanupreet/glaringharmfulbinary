n, k = [int(x) for x in input().split()]
count = 0
nums = [int(x) for x in input().split()]
for i in range(n):
    if nums[i] > 0 and nums[i] >= nums[k-1]:
        count += 1
    else:
        break
print(count)
