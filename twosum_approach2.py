input_array = [2, 3, 6, 1, 8, 9]
input_target = 10


def twosum(nums, target):
    for i in range(len(nums)):
        new_target = target - nums[i]
        for j in range(len(nums)):
            if i != j:
                if nums[j] == new_target:
                    return [i, j]


print(twosum(input_array, input_target))
