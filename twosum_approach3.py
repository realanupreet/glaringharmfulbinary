input_array = [2, 3, 6, 1, 8, 9]
input_target = 10


def twosum(nums, target):
    nummap = {}
    for i in range(len(nums)):
        num = nums[i]
        if target - num in nummap:
            return [nummap[target-num], i]
        nummap[num] = i


print(twosum(input_array, input_target))
