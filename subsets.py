nums = [1, 2, 3]


def subset(nums):
    res = []

    subset = []

    def dfs(i):  # 0
        # print(f"i is {i}")
        if i >= len(nums):
            res.append(subset.copy())
            # print("res is", res)
            return

        subset.append(nums[i])
        # print(f"subset appended becomes {subset}")
        dfs(i+1)

        subset.pop()
        # print(f"subset popped becomes {subset}")
        dfs(i+1)

    dfs(0)
    return res


print(subset(nums))
