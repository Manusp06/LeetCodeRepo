class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        md = float('inf')
        res = -1
        for i,j in enumerate(points):
            if j[0]==x or j[1]==y:
                d = abs(x-j[0]) + abs(y-j[1])
                if d < md :
                    md = d
                    res = i
        return res