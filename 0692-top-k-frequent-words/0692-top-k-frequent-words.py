class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        ans = {}
        for i in words:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        key = list(ans.keys())
        value = list(ans.values())
        combine = list(zip(value,key))
        combine.sort(reverse = True)
        value ,key = zip(*combine)
        value = list(value)
        key = list(key)
        values = list(dict.fromkeys(value))
        if len(values) == len(value):
            return key[:k]
        # temp = []
        # dum = 0
        else:
            for i in values:
                if value.count(i) != 1:
                    dum = value.count(i)
                    ind = value.index(i)
                    temp = key[ind:ind+dum]
                    temp.sort()
                    key[ind:ind+dum] = temp
            return key[:k]
                    




        