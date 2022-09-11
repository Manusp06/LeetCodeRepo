class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[0:n]
        y = nums[n:len(nums)]
        l1 = list(zip(x,y))
        l1 = [j for i in l1 for j in i]
        return l1


#Success
Details 
Runtime: 60 ms, faster than 96.38% of Python3 online submissions for Shuffle the Array.
Memory Usage: 14.2 MB, less than 40.76% of Python3 online submissions for Shuffle the Array.