class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            ind = word.index(ch)
            temp = word[:ind+1]
            word = temp[::-1] + word[ind+1:]
            return word
        else:
            return word
        
        