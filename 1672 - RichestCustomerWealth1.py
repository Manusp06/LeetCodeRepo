class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1 = 0
        for i in accounts:
            a = sum(i)
            if a > sum1:
                sum1 = a
        return sum1