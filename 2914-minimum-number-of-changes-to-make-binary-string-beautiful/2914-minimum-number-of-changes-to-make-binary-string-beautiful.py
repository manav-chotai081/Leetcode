class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s), 2):
            temp = s[i] + s[i+1]
            if temp == '10' or temp == '01':
                count += 1
        return count
        