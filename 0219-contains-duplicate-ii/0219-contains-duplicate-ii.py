class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = {}
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans[nums[i]] = i
            else:
                if abs(ans[nums[i]] - i) <= k:
                    return True
                else:
                    ans[nums[i]] = i
        return False 
        