class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = []
        for i in s:
            if i in 'AEIOUaeiou':
                vowel.append(i)
        vowel.sort()
        count = 0
        s1 = ''
        for i in range(len(s)):
            if s[i] in 'AEIOUaeiou':
                s1 += vowel[count]
                count += 1
            else:
                s1 += s[i]
        return s1


        