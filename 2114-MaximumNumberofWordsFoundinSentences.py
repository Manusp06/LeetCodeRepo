class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l1 = []
        for i in sentences:
            c = i.split(" ")
            d = len(c)
            l1.append(d)
            c=''
            d=0
        return max(l1)
        
        
        m = 0
        for i in sentences:
            c = 0
            for j in i:
                if j==' ':
                    c+=1
                m = max(m, c+1)
        return m