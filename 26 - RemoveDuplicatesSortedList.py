class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        a = dict.fromkeys(nums)
        nums[:len(a)]=a
        return len(a)
        