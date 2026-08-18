class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words = words1 + words2
        word = list(set(words))
        count = 0
        for i in word:
            if words1.count(i) == 1 and words2.count(i) == 1:
                count += 1
        return count
        