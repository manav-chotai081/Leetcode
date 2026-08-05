class Solution:
    def maxArea(self, height: List[int]) -> int:
        len1 = len(height)
        right = len1 - 1 
        left = 0
        ans = []
        while left < right:
            value = min(height[left], height[right])
            ans.append(value*(right - left))
            if value == height[left]:
                left += 1
            else:
                right -= 1
        return max(ans)
        