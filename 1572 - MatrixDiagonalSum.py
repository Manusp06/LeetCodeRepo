class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum1=0
        for i in range(0,n):
            for j in range(0,n):
                if(i==j) or (j+i==(n-1)):
                    sum1+= mat[i][j]
        return sum1