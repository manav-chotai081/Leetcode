class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = list(set(nums))
        count = []
        for i in num:
            count.append(nums.count(i))
        for i in range(len(num)):
            if count[i] > 2:
                for j in range(2,count[i]):
                    nums.remove(num[i])
        return len(nums)
        