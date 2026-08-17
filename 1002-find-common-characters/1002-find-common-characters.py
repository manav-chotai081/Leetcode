class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        count = 0
        for i in words[0]:
            for j in range(len(words)):
                if i in words[j]:
                    count += 1
                    words[j] = words[j].replace(i,'',1)
                    if count == len(words):
                        ans.append(i)
                        count = 0
                else:
                    count = 0
                    break
        return ans
        