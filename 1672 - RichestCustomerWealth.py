class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l1 = []
        c = 0
        for i in accounts:
            c = sum(i)
            l1.append(c)
            c = 0
        return max(l1)
        
        #solution 2
        return max([sum(i) for i in accounts])
        