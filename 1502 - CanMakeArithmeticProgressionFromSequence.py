class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for x,y in zip(arr, arr[1:]):
            if y-x != arr[1]-arr[0] :
                return False
        return True
       