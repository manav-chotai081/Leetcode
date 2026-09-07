class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = []
        temp = 0
        s = ''
        for i in nums:
            ans.append(i)
            # temp = 0
            # while i > 0:
            #     temp *= 10
            #     temp += i % 10
            #     i = i // 10
            s = str(i)
            temp = int(s[::-1])
            ans.append(temp)
        return len(list(set(ans)))
                

        