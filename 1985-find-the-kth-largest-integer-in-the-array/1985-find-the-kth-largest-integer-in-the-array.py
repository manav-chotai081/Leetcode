class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num = []
        for i in nums:
            num.append(int(i))
        num.sort()
        return str(num[len(num)-k])
        