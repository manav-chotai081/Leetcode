class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # w1 = s1.split()
        # w2 = s2.split()
        # w = w1+w2
        # ans = []
        # for i in w:
        #     if i in w1 and i in w2:
        #         pass
        #     else:
        #         ans.append(i)
        # return ans



        w1 = s1.split()
        w2 = s2.split()
        # ans1 = []
        # for i in w1:
        #     if i not in ans1 and w1.count(i) == 1:
        #         ans1.append(i)
        # ans2 = []
        # for i in w2:
        #     if i not in ans2 and w2.count(i) == 1:
        #         ans2.append(i)
        # ans = []
        # for i in ans1:
        #     if i not in ans2:
        #         ans.append(i)
        # for i in ans2:
        #     if i not in ans1:
        #         ans.append(i)
        # return ans

        w = w1 + w2
        ans = []
        for i in w:
            if w.count(i) == 1:
                ans.append(i)
        return ans

        
        
        