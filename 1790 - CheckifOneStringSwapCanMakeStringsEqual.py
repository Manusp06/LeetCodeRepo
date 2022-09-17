class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if sorted(s1)!=sorted(s2):
            return False
        
        c = 0
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                c+=1
        if c<3:
            return True
        else:
            return False
        





#Runtime: 34 ms, faster than 91.04% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
Memory Usage: 13.9 MB, less than 72.80% of Python3 online submissions for Check if One String Swap Can Make Strings Equal.
Next challenges: