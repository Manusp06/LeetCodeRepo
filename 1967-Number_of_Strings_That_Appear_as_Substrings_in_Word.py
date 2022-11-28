class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        c = 0
        
        for i in patterns:
            if i in word:
                c+=1
                
        return c
        


Runtime: 31 ms, faster than 99.04% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
Memory Usage: 14 MB, less than 36.12% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.