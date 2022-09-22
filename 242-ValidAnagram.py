class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution 1
        s = sorted(s)
        t = sorted(t)
        if s==t:
            return True
        
        #solution2
        dict_s = {}
        dict_t = {}
        
        for i in s:
            if not i in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i]+=1
        
        for j in t:
            if not j in dict_t:
                dict_t[j] = 1
            else:
                dict_t[j]+=1
        
        if dict_s==dict_t:
            return True
        else:
            return False
        