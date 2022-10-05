class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        j = 0
        target = []*(len(nums))
        for i in range(0,len(nums)):
            a = index[i]
            b = nums[i]
            target.insert(a,b)
        return target