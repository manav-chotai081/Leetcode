class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = []
        for i in range(len(accounts)):
            ans.append(sum(accounts[i]))
        return max(ans)
        