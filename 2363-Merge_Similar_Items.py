class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        
        d = {}
        
        for i in items1:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]+=i[1]
                
        for i in items2:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]+=i[1]
        
        l = []
        for k,j in d.items():
            l.append([k,j])
        
        return sorted(l)
        
        
        for i in items1:
            for j in items2:
                if i[0] == j[0]:
                    i[1] = i[1]+j[1]
                    items2.remove(j)
                    
        return sorted(items1 + items2)

           
        
    
    