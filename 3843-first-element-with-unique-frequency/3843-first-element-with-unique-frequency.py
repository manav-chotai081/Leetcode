class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        times = list(freq.values())
        element = list(freq.keys())
        time = list(dict.fromkeys(times))
        for i in time:
            if times.count(i) == 1:
                return element[times.index(i)]
        return -1

        