class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total =0
        result = 0

        for i in accounts:
            total = sum(i)
            result = max(total, result)
        return result  

# Time:  O(m * n)
# Space: O(1)