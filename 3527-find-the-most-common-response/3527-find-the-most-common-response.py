class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans = {}
        for i in responses:
            temp = list(set(i))
            for j in temp:
                if j not in ans:
                    ans[j] = 1
                else:
                    ans[j] += 1
        # combine = list(zip(ans.values(), ans.keys())).sort()

        value = list(ans.values())
        key = list(ans.keys())
        max1 = max(value)
        ind = value.index(max1)
        times = value.count(max1)
        if times > 1:
            combine = list(zip(value,key))
            combine.sort(reverse = True)
            value, key = zip(*combine)
            value = list(value)
            key = list(key)
            temp = key[:times]
            return min(temp)
            
        return key[ind]
        