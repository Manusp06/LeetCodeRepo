class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1 = s[0:1]
        r1 = s[1:2]
        c2 = s[3:4]
        r2 = s[4:]
        l1 = []
        
        for i in range(ord(c1), ord(c2)+1):
            x = chr(i)
            for j in range(int(r1), int(r2)+1):
                y = x + str(j)
                l1.append(y)
                
        return l1