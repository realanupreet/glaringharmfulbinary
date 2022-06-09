nums = [2, 0, 2, 1, 1, 0]

n = len(nums)

for i in range(len(nums)):
    if nums[i] == 0:
        nums.pop(i)
        nums = [0] + nums
    elif nums[i] == 2:
        nums.pop(i)
        nums = nums + [2]


def sortitup(nums):
    n = len(nums)

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums = [0] + nums
        elif nums[i] == 2:
            nums.pop(i)
            nums = nums + [2]
    return nums


print(sortitup(nums))
