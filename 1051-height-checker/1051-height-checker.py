class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0
        height = sorted(heights)
        for i in range(len(heights)):
            if height[i] != heights[i]:
                count += 1
        return count
        