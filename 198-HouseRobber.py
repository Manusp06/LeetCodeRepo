class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums : return 0
        if len(nums)<3 : return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
            
        return dp[-1]





class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Initialise rob1 and rob2 at 0, then for each val in nums, calculate the max of 
        (n+rob1), representing robbing that house and missing the one before it, and rob2, 
        the house before it. Update rob1 to be rob2 and rob2 to be the maximal value that 
        can be robbed, which is subsequently returned.
        
        :param: nums: the array of numbers to be considered. (List[int])
        :return: rob2: the maximal value to be considered. (int)
        """
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2