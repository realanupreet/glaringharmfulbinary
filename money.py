n = 4
nums = [3, 1, 5, 8]
# 0 1  2  3
# 3 15 40 40
snums = [1]+nums+[1]

# tnum = nums
# tsnum = snums
for i in range(len(nums)):
    tnum = nums.copy()
    print(i)
    for j in range(len(tnum)):
        tsnum = [1] + tnum + [1]
        print(" ", j, tsnum, tnum)
        if i < len(tnum):
            tnum.pop(i)
        else:
            tnum.pop()
        # print(" ",j,tsnum,tnum)
