class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        ans1 = []
        ans2 = []
        for i in range(len(nums)):
            if i % 2== 0:
                ans1.append(nums[i])
            else:
                ans2.append(nums[i])
        ans1.sort()
        ans2.sort(reverse = True)
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = ans1[count1]
                count1 += 1
            else:
                nums[i] = ans2[count2]
                count2 += 1
        return nums       