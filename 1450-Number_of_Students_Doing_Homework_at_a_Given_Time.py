class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        c = 0
        
        for x,y in zip(startTime, endTime):
            if x<= queryTime <= y:
                c+=1
                
        return c