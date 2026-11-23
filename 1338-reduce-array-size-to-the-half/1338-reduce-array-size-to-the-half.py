class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        times = {}
        for i in arr:
            if i in times:
                times[i] += 1
            else:
                times[i] = 1
        value = list(times.values())
        count = 0
        value.sort(reverse = True)
        total = sum(value)
        len1 = len(arr)
        for i in value:
            total -= i
            count += 1
            if total <= (len1 // 2):
                return count
        
        
        