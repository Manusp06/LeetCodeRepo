class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for num in nums:
            length = floor(log10(num)+1)
            if length%2 == 0:
                count+=1
        return count