class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current=0
        ans=0
        for i in gain:
            current=current +i
            ans=max(ans,current)
        return ans    
#time O(n)
#spaceO(1)
