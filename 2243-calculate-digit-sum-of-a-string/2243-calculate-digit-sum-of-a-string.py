class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            dummy = ''
            len1 = len(s)
            for i in range(0, len(s), k):
                temp = 0
                for j in range(i, i + k):
                    if j < len1:
                        temp += int(s[j])
                dummy += str(temp)
            s = dummy
        return s
                
        