class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operators = {"++X" : 1, "X++" : 1, "--X" : -1, "X--" : -1}
        return sum(operators[i] for i in operations)


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum = 0
        for i in operations :
            if i== ("++X") or i == ("X++"):
                sum+=1
            else:
                sum-=1
        return sum