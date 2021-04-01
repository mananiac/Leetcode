class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.arr3 = [[-1 for x in range(1001)] for y in range(1001)]
        self.arr1 = text1
        self.arr2 = text2
        return self.lcs(0,0,self.arr1,self.arr2,self.arr3)
        
    def lcs(self,i,j,arr1,arr2,arr3):
        if (i>=len(arr1) or j>=len(arr2)):
            return 0
        if (arr1[i]==arr2[j]):
            self.hello=self.lcs(i+1,j+1,arr1,arr2,arr3)
            self.hello=self.hello+1
            return self.hello
        if arr3[i][j] != -1:
            return arr3[i][j]
        else:
            self.left,self.right = self.lcs(i+1,j,arr1,arr2,arr3),self.lcs(i,j+1,arr1,arr2,arr3) 
             
            arr3[i][j] = max(self.left,self.right)
            return arr3[i][j]