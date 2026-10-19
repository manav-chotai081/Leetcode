class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        if target in nums:
            nums.sort()
            times = nums.count(target)
            ind = nums.index(target)
            count = ind
            ans = []
            for i in range(times):
                ans.append(count)
                count += 1
            return ans
        return []

        
        