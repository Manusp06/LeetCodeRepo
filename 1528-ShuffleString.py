class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        j = 0
        m=''
        
        for i in indices:
            d[i] = s[j]
            j+=1
        
        d = dict(sorted(d.items()))
        
        for i in d.keys():
            m+=d[i]
            
        return m