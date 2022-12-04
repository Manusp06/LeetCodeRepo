class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        s = coordinates
        a = 97
        d = {}
        
        for i in range(1,9):
            c = chr(a)
            d[c] = i
            a+=1
            
        
        if (int(d[s[0]])%2!=0 and int(s[1]) %2!=0 ) or (int(d[s[0]])%2==0 and int(s[1]) %2==0 ):
            return False
        else:
            return True





Success
Details 
Runtime: 37 ms, faster than 85.70% of Python3 online submissions for Determine Color of a Chessboard Square.
Memory Usage: 14 MB, less than 9.28% of Python3 online submissions for Determine Color of a Chessboard Square.