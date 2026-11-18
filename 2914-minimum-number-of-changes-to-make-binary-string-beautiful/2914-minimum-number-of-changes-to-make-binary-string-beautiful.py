class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s), 2):
            temp = int(s[i] + s[i+1])
            if temp == 10 or temp == 1:
                count += 1
        return count
        