class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        d = {}
        l1 = []
        
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                
        for j in d:
            if d[j]==1:
                l1.append(j)
        return sum(l1)