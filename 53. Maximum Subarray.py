class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a,b=float('-inf'),float('-inf')
        for num in nums:
            a=max(a+num,num)
            b=max(b,a)
        return b

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #KADANE 
        res = float('-inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res = max(res,total)
            if total < 0:
                total = 0
        return res


# time O(n)
# space O(1)