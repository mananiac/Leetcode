class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        dic = {}

        for i in sentence:
            if i in dic:
                dic[i] = dic[i] +1
            else:
                dic[i] = 1
            
        return(len(dic)==26)

# Time:  O(n)
# Space:  O(1)        