class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while(n!=1):
            if n%2==0:
                n=n//2
                count = count+n
            else:
                n=(n-1)//2
                count = count+n
                n=n+1
        return count    

# time O(logN)
# space O(1)
 

 class Solution2:
    def numberOfMatches(self, n: int) -> int:
        return n-1

# Time:  O(1)
# Space: O(1)        