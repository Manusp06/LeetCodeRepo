class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l1 = []
        l1_prod = 1
        while(n>0):
            rem = n%10
            l1.append(rem)
            n = n//10
        l1_sum = sum(l1)
        for i in l1:
            l1_prod *= i
        return l1_prod - l1_sum
            