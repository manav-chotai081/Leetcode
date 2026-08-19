class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        num = list(set(nums))
        ans = []
        for i in num:
            if i % 2 == 0:
                ans.append(i)
        count = []
        if len(ans) == 0:
            return -1
        for i in ans:
            count.append(nums.count(i))
        ans1 = []
        max1 = max(count)
        count1 = count.count(max1)
        for i in range(count1):
            temp = count.index(max1)
            ans1.append(ans[temp])
            count[temp] = -1
        return min(ans1)
        
        