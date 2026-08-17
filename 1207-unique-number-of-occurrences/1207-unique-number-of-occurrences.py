class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num = list(set(arr))
        count = []
        for i in num:
            count.append(arr.count(i))
        c1 = list(set(count))
        if len(c1) == len(count):
            return True
        return False
        