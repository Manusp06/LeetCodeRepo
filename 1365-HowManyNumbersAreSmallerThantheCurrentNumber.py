class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l1 = []
        a = sorted(nums)
        for i in nums:
            l1.append(a.index(i))
        return l1
            