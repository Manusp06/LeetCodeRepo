class Solution:
    def average(self, salary: List[int]) -> float:
        min_1 = min(salary)
        max_1 = max(salary)
        l1 = []
        for i in salary:
            if i!=min_1 and i!=max_1:
                l1.append(i)
        return mean(l1)
        
Runtime: 26 ms, faster than 98.88% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
Memory Usage: 14 MB, less than 9.89% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.