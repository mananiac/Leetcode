class Solution:
    def isHappy(self, n: int) -> bool:
        def Manan(n):

            result =0
            while(n>0):

                r=n%10
                result = result +r*r
                n=n//10
            return result   
        
        seenSet = set()

        while Manan(n) not in seenSet:
            boogabooga=Manan(n)
            if boogabooga == 1:
                return True
            else:
                seenSet.add(boogabooga)
                n= boogabooga
        return False       


