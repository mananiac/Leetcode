class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if (m == 0): 
            return 0
        n = len(matrix[0])
        height=0
        arr = [[0]*(n+1) for _ in range (m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1] == "1"):
                    arr[i][j] = 1 + min(arr[i-1][j],arr[i-1][j-1],arr[i][j-1])
                    height = max(arr[i][j],height)
        return height**2    
        