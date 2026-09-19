class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        ans1 = {}
        ans = []
        temp = []
        for i in nums:
            if i not in ans1:
                ans1[i] = 1
            else:
                ans1[i] += 1
        key = list(ans1.keys())
        value = list(ans1.values())
        combine = list(zip(value, key))
        combine.sort()
        value, key = zip(*combine)
        key = list(key)
        value = list(value)
        v = list(dict.fromkeys(value))
        count = 0
        for i in v:
            if value.count(i) == 1:
                for i in range(value[count]):
                    ans.append(key[count])
                count += 1
            else:
                times = value.count(i)
                temp = key[count:count+times]
                temp1 = value[count:count+times]
                combine = list(zip(temp, temp1))
                combine.sort(reverse = True)
                temp, temp1 = list(zip(*combine))
                for i in range(len(temp)):
                    for j in range(temp1[i]):
                        ans.append(temp[i])
                    count += 1
        return ans




        