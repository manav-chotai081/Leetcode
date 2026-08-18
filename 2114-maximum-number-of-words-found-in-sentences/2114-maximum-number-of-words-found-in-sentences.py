class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1= 0
        for i in sentences:
            ans = i.split()
            if len(ans)>max1:
                max1 = len(ans)
        return max1

        