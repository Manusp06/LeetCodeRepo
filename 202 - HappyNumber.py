class Solution:
    def isHappy(self, n: int) -> bool:
        while(len(str(n)))!=1:
            arr = [int(i)**2 for i in str(n)]
            n = sum(arr)
        if n==1 or n==7:
            return True
        else:
            return False