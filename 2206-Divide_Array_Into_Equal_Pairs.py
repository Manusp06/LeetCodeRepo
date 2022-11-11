class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        d = {}
        
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
                
        for i,j in d.items():
            if j%2!=0:
                return False
            
        return True
        