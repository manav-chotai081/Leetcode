class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ans = ''
        # if s[::] == s[::-1]:
        #     return s
        # for i in range(len(s)):
        #     temp = s[i:]
        #     temp = temp[::-1]
        #     for j in range(i, len(s)):
        #         if temp[i:] == temp[len(s)-1:i-1:-1]:
        #             if len(temp[i:])> len(ans):
        #                 ans = temp[i:]
        #             else:
        #                 break
        # return ans


        ans = ''
        for i in range(len(s)):
            temp = len(s)
            for j in range(i,len(s)):
                ans1 = s[i:temp]
                if ans1 == ans1[::-1]:
                    if len(ans1) > len(ans):
                        ans = ans1
                    break
                temp -= 1
        return ans

        