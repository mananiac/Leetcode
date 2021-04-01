class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        c1,c2=0,0
        for i in range(len(s1)):
            c1,c2=c1+ord(s1[i]),c2+ord(s2[i])
        s1=sorted(list(s1))
        s2=sorted(list(s2)) 
        
        for i in range(len(s1)):
            if c1>=c2:
                if s1[i] >=s2[i]:
                    continue
                else:
                    return False
            if c1<c2:
                if s1[i] <=s2[i]:
                    continue
                else:
                    return False
        return True