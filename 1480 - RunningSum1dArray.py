class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in range(0,len(nums)):
            if i==0:
                nums1.append(nums[i])
            else:
                nums1.append(nums[i]+nums1[i-1])
        return nums1