class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        count = 0
        l1 = list(range(1, n+1))
        for i in l1:
            ans.append('Push')
            count += 1
            if i not in target:
                ans.append('Pop')
            if count == target[len(target)-1]:
                break
        return ans
        