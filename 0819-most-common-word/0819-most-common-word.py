class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        ans = paragraph.split()
        max1 = ''
        freq = 0
        ans1 = list(set(ans))
        for i in banned:
            if i in ans1:
                ans1.remove(i)
        for i in ans1:
            temp = ans.count(i)
            if temp > freq:
                freq = temp
                max1 = i
        return max1
                



