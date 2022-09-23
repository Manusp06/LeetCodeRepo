class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l1 = nums
        l2 = []
        cur_sum = 0
        for i in l1:
            cur_sum+=i
            if cur_sum < 0 :
                cur_sum = 0
            else:
                l2.append(cur_sum)
                
        if len(l2)==0:
            return max(l1)
        else:
            return max(l2)