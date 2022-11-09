class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in range(len(nums)):
            # print(n,nums[nums[n]])
            ans.append(nums[nums[n]])
        return ans
