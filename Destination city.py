class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pathSet = set()
        d1=[]
        d2=[]
        dic= {}
        for i in range(len(paths)):
            for j in range(2):
                d1.append(paths[i][0])
                d2.append(paths[i][1])
        
        for i in range(len(d1)):
            if (d2[i] in d1):
                continue
            else    :
                return (d2[i])
         