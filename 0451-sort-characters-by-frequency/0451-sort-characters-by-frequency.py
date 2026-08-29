class Solution:
    def frequencySort(self, s1: str) -> str:
        s1 = s1.replace('', ' ')
        char = s1.split()
        char = list(set(char))
        freq = []
        for i in char:
            freq.append(s1.count(i))
        combined = list(zip(freq,char))
        combined.sort(reverse = True)
        freq,char = zip(*combined)
        s = ''
        for i in range(len(freq)):
            for j in range(freq[i]):
                s += char[i]
        return s
                
        

        