class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        key = []
        value = []
        temp = ''
        for i in arr:
            key.append(i)
            temp = ''
            # if i == 0:
            #     ans[i] = 0
            while i > 0:
                temp += str(i % 2)
                i = i // 2
            value.append(temp.count('1'))
        combine = list(zip(value,key))
        combine.sort()
        value, key = zip(*combine)
        return key
            
        

        