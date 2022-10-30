class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        p = len(pref)
        c = 0
        for i in words:
            if i[0:p] == pref:
                c+=1
            
        return c