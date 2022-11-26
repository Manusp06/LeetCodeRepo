class Solution:
    def replaceDigits(self, s: str) -> str:
        
        s1 = ''
        for i in range(0,len(s)):
            if s[i].isnumeric():
                s1 += chr(ord(s[i-1]) + int(s[i]))
            else:
                
                s1 += s[i]
                
        
        return s1