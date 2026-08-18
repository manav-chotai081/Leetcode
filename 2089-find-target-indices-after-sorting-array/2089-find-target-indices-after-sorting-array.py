class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        count = nums.count(target)
        ans = []
        if count < 1:
            return ans
        ind = nums.index(target)
        for i in range(count):
            ans.append(ind)
            ind += 1
        return ans
        