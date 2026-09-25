class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        # return min(len(nums1)//2, len(num1)) + min(len(nums1)//2, len(num2))
        ans = {}
        num = num1 + num2
        for i in num:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        if len(num1) <= len(nums1)//2 and len(num2) <= len(nums1)//2:
            return len(list(ans.keys()))
        else:
            n = min(len(num1), len(nums1)//2) + min(len(num2), len(nums1)//2)
            key = list(ans.keys())
            value = list(ans.values())
            combine = list(zip(value,key))
            combine.sort()
            value,key = list(zip(*combine))
            key = list(key)
            
            return len(key[:n])

            

            
