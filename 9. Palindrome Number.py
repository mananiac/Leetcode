class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        i=0
        j=len(s)-1
        while i< j:
            if s[i] != s[j] : 
                return False
            else:
                i+=1
                j-=1
        return True     
# time O(n)
# space O(1)

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x<0:
            return False
        num =0 
        while x is not 0:
            a = x%10
            x=x//10
            num = num*10 +a
        if num==   original:
            return True
        else:
            return False

# time O(logn)
# space O(1)