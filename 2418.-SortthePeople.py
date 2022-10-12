class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap1 = {}
        l1 = []
        
        for i in range(len(heights)):
            hashmap1[heights[i]] = names[i]
            
        heights.sort(reverse = True)
        
        for i in range(len(heights)):
            names[i] = hashmap1[heights[i]]
            
        return names
        