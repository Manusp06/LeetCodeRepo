class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        elif x < 10 :
            return True
        else:
            rev = 0
            rem = x%10
            quot = x//10
            rev = rev*10+rem
            while(quot >= 10):
                rem = quot%10
                quot = quot // 10
                rev = rev*10+rem
            rev=rev*10+quot
            if x==rev:
                return True
            else:
                return False