class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
    
        l1 = []
        l2 = []
        
        for i in nums:
            if i%2==0:
                l1.insert(0,i)
            else:
                l2.append(i)
                
        return l1+l2
        