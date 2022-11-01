class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        d = Counter(nums)
        cnt = [0, 0]
        for i, j in d.items():
            cnt[0] += j//2
            cnt[1] += j%2
        return cnt
        
        
        nums.sort()
        cnt,i = 0, 1
        
        while i<len(nums):
            if nums[i]==nums[i-1]:
                cnt+=1
                i+=1
            i+=1
            
        return (cnt, len(nums)-2*cnt)
        