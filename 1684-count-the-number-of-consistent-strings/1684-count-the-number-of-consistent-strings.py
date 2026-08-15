class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            temp = []
            for j in words[i]:
                temp.append(j)
            for j in range(len(temp)):
                if temp[j] in allowed:
                    if j == len(temp)-1:
                        ans += 1
                else:
                    break
        return ans
                
        