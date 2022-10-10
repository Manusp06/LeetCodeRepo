class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        soln = []
        for i in range(n-2):
            a = []
            for j in range(n-2):
                mx = max(max(grid[i][j:j+3]),max(grid[i+1][j:j+3]),max(grid[i+2][j:j+3]))
                a.append(mx)
                
            soln.append(a)
        return soln
        