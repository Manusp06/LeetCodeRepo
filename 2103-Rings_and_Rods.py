class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        c = 0
        
        
        for i in range(1,len(rings),2):
            if rings[i] not in d:
                d[rings[i]] = rings[i-1]
            else:
                d[rings[i]]+= (rings[i-1])
                
                
        for i,j in d.items():
            if 'R' in j and 'G' in j and 'B' in j:
                c+=1
                
                
        return c
                
        