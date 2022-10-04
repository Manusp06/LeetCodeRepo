class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l1 = []
        for i in range(0,len(nums)):
            if i%2==0:
                a = nums[i]
                b = nums[i+1]
                for i in range(a):
                    l1.append(b)
        return l1