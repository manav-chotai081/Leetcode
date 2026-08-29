# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans1 = []
        while head != None :
            ans1.append(head.val)
            head = head.next
        ans2 = []
        for i in range(len(ans1)):
            ans2.append(ans1[i])
            if i < len(ans1) - 1:
                a = ans1[i]
                b = ans1[i+1]
                while True:
                    if b == 0:
                        break 
                    temp = a
                    a = b
                    b = temp % b
                ans2.append(a)
        ans = ListNode(0)
        dummy = ans
        for i in ans2:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans


        