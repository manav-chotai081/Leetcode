class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
        temp = nums.count(pivot)
        ans = less[:]
        for i in range(temp):
            ans.append(pivot)
        for i in greater:
            ans.append(i)
        return ans
        