class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tr = sum(nums)
        if tr % 2 != 0:
            return False

        tr = tr/2
        t = {}

        def subsetSum(n, tr):
            if tr == 0:
                return True
            if n == 0:
                return False
            if (n, tr) in t:
                return t[(n, tr)]
            if nums[n-1] <= tr:
                t[(n, tr)] = subsetSum(n-1, tr-nums[n-1]) or subsetSum(n-1, tr)
                return t[(n, tr)]
            else:
                t[(n, tr)] = subsetSum(n-1, tr)
                return t[(n, tr)]

        return subsetSum(len(nums), tr)
