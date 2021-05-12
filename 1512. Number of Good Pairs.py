class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        dic={}
        for i in nums:
            if i in dic:
                dic[i] = dic[i] +1
            else:
                dic[i]=1
        for i in dic:
            count= count+((dic[i]*(dic[i]-1))//2)
        return count   

# time O(n)
# space O(n)