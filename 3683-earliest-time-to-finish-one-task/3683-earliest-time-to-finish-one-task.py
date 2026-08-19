class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = []
        for i in range(len(tasks)):
            ans.append(sum(tasks[i]))
        return min(ans)
        