class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        num = list(set(nums))
        count = []
        for i in num:
            count.append(nums.count(i))
        ans = 0
        for i in range(len(count)):
            if count[i] % k == 0:
                ans += count[i]*num[i]
        return ans

        