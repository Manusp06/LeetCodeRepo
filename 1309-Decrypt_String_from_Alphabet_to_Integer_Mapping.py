class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        ans = ''
        i = 0
        
        while i < len(s):
            if i+2 < len(s):
                if s[i+2] == '#':
                    temp = int(s[i] + s[i+1]) + 96
                    ans = ans + chr(temp)
                    i += 3
                else:
                    
                    temp = int(s[i]) + 96
                    ans = ans + chr(temp)
                    i +=1
                    
            else:
                temp = int(s[i]) + 96
                ans = ans + chr(temp)
                i +=1
            
            
        return ans
                
                
       
    
    