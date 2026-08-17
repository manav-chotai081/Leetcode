class Solution:
    def average(self, salary: List[int]) -> float:
        max1 = max(salary)
        min1 = min(salary)
        ans = 0
        count = 0
        for i in salary:
            if i == min1 or i == max1:
                pass
            else:
                ans+= i
                count += 1
        return ans/count
        