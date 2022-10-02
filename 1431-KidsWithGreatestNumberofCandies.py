class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l1 = []
        a = max(candies)
        for i in candies:
            if i+extraCandies >= a:
                l1.append(True)
            else:
                l1.append(False)
        return l1