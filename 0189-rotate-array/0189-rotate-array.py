class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # a=[]
        # b=[]
        # n=len(nums)
        # a = nums[:n-k]
        # b = nums[n-k-1:n:]
        # nums = []
        # nums = b[::]
        # for i in a:
        #     nums.append(i)
        len1 = len(nums)
        k = k % len1
        ans = []
        for i in range(len1-1, len1-k-1,-1):
            ans.append(nums[i])
        for i in range(k):
            nums.insert(0, ans[i])
        for i in range(k):
            nums.pop()











        """
        Do not return anything, modify nums in-place instead.
        """
        