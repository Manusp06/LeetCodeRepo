class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        l1 = [0]
        
        for i in gain:
            l1.append(i+l1[-1])
            
        return max(l1)