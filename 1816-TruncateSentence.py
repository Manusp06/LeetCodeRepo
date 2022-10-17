class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        s1=''
        l = []

        for i in range(0,k):
            l.append(s[i])

        le =  len(l)
        for j in range(0,len(l)):
            if j!=len(l)-1:
                s1+=l[j]
                s1+=' '
            else:
                s1+=l[j]

        return s1
            
    

solution 2
---------------
return ' '.join(s.split()[:k])
        