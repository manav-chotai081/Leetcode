class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # for i in target:
        #     if i not in arr:
        #         return False
        # return True

        ans1 = {}
        for i in target:
            if i in ans1:
                ans1[i] += 1
            else:
                ans1[i] = 1
        ans2 = {}
        for i in arr:
            if i in ans2:
                ans2[i] += 1
            else:
                ans2[i] = 1
        for i,j in ans1.items():
            if i not in ans2:
                return False
            elif i in ans2 and ans2[i] != j:
                return False
        return True


        