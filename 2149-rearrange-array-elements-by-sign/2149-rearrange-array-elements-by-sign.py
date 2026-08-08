class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         if nums[i] < 0:
        #             for j in range(i, len(nums)):
        #                 if nums[j] > 0:
        #                     temp = nums[i]
        #                     nums[i] = nums[j]
        #                     nums[j] = temp
        #                     break
        #     else:
        #         if nums[i] > 0:
        #             for j in range(i, len(nums)):
        #                 if nums[j] < 0:
        #                     temp = nums[i]
        #                     nums[i] = nums[j]
        #                     nums[j] = temp
        #                     break


        # return nums

        pos = []
        neg = []
        ans = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(pos[c1])
                c1 += 1
            else:
                ans.append(neg[c2])
                c2 += 1
        return ans


                            


        