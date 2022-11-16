class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        letters = 'abcdefghijklmnopqrstuvwxyz'
        l = ''
        s1 =''
        
        for i in key:
            if i not in l and i!=' ':
                l+=i
                
        d = dict(zip(l,letters))
                
        for i in message:
            if i!=' ':
                s1+= d[i]
            else:
                s1+= ' '
                
        
        return s1