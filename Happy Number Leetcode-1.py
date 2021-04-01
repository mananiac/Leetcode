class Solution(object):
    
    
    def isHappy(self, n):
        def sol(num,sumo):
            try:

                for i in num:
                    sumo=sumo+i**2
                num = list(map(int,str(sumo)))
                if (sumo == 1):
                    return True
                # print(num,sumo)
                sumo =0
                return sol(num,sumo)    
            except: 
                return False


        num =list(map(int, str(n)   ) )
        # print(num)
        sumo =0
        hello = sol(num,sumo) 
        return hello