class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        l1 = []
        
        for i in image:
            l1.append(i[::-1])
            
        for j in l1:
            le = len(j)
            for k in range(le):
                if j[k]==1:
                    j[k]=0
                else:
                    j[k]=1
                    
        return l1