# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1 != None:
            num1 *= 10
            num1 += l1.val
            l1 = l1.next
        num2 = 0
        while l2 != None:
            num2 *= 10
            num2 += l2.val
            l2 = l2.next
        num = num1 + num2
        num = str(num)
        ans = ListNode(0)
        dummy = ans
        for i in num:
            ans.next = ListNode(int(i))
            ans = ans.next
        ans = dummy.next
        return ans



        