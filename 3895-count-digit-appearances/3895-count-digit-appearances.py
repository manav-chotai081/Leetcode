class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for i in nums:
            copy = i
            while copy > 0:
                if copy % 10 == digit:
                    count += 1
                copy = copy // 10
        return count

        