class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        l=len(s)
        
        s = s.lower()
        
        s1 = s[0:l//2]
        s2 = s[l//2:l]
        
        c,c1 = 0,0
        
        vowels = 'aeiou'
        
        for i in s1:
            if i in vowels:
                c+=1
                
        for j in s2:
            if j in vowels:
                c1+=1
                
        if c==c1:
            return True
        
        else:
            return False
        