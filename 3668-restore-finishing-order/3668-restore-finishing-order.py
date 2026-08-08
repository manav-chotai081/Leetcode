class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        count = 0
        len1 = len(order)
        len2 = len(friends)
        ans = []
        for i in range(len1):
            if order[i] in friends:
                ans.append(order[i])
                count += 1
            elif count == len2:
                break
        return ans


        