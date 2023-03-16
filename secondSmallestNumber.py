# User function Template for python3
class Solution:
    def secondSmallest(self, S, D):
        # remaining S
        rem = S
        ans = ""
        # reserving for most significant bit
        rem -= 1
        # find smallest element first
        for i in range(D):
            ans = str(min(9, rem))+ans
            rem -= min(9, rem)
            # adding most significant bit
            if i == D-2:
                rem += 1
        # converting smallest element to second smallest element
        for i in range(D-1, -1, -1):
            # adding 1 to ans[-1] and subtracting 1 from ans[-2]
            if ans[i] != '0' and ans[i-1] < '9':
                x = int(ans[i])-1
                ans = ans[:i]+str(x)+ans[i+1:]
                x = int(ans[i-1])+1
                ans = ans[:i-1]+str(x)+ans[i:]
                break
        if i == 0:
            return "-1"
        return ans
