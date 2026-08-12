class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for i in range(len(points)):
            temp = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            ans.append(temp**0.5)
        ans1 = []
        for i in range(k):
            temp = min(ans)
            ind = ans.index(temp)
            ans[ind] = float('inf')
            row = []
            row.append(points[ind][0])
            row.append(points[ind][1])
            ans1.append(row)
        return ans1
        