class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = 0
        s = ''
        for i in words:
            ans = 0
            for j in i:
                temp = ord(j) - 97
                ans += weights[temp]
            ans = ans % 26
            val = 26 - ans + 96
            s += chr(val)
        return s
            
                

        