class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        n = len(arr)
        for i in range(0,n):
            for j in range(i+1,n+1):
                if(j-i)%2!=0:
                    ans += sum(arr[i:j])
        return ans
            