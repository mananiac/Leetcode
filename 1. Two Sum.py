class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        manan = dict()
        i=0

        for num in nums:
            if num in manan:
                return [manan[num],i]
            else:
                manan[target-num]=i
                i=i+1

# time and space complexity: O(n)
