class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l1 = [first]
        for i in encoded:
            l1.append(l1[-1]^i)
        return l1
        