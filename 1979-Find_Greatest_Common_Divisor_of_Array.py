class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        c = 0
        nums = sorted(nums)
        
        small = nums[0]
        large = nums[-1]
        
        for i in range(1, small+1):
            if small%i==0 and large%i==0:
                c=i
                
        
        return c
        