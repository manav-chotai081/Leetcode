class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            temp = ''
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    break
            if len(temp) > ans:
                ans = len(temp)
        return ans


        