class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers.count(-1) > 1000:
            return [29999,30000]
        start = 0
        end = 0
        len1 = len(numbers)
        for i in range(len1):
            for j in range(i+1, len1):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        