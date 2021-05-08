class Solution:
    def validPalindrome(self, s: str) -> bool:

        left=0
        right=len(s)-1
        count =0
        def sol(s,left, right):
            while(left<right):
                if s[left] != s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True       

        while left<right:
            if s[left] != s[right]:
                return sol(s,left+1,right) or sol(s,left,right-1)
            else:
                left+=1
                right-=1
        return True        

# time: O(N)
# space O(1)        