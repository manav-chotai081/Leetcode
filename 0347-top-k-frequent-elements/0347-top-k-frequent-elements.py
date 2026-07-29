class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = list(set(nums))
        count = []
        ans = []
        for i in range(len(num)):
            count.append(nums.count(num[i]))
        for i in range(k):
            temp = max(count)
            value = count.index(temp)
            ans.append(num[value])
            count[value] = -1
        return ans

        