# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0:
            return ListNode(0)
        ans = 0
        while head != None:
            ans *= 10
            ans += head.val
            head = head.next
        ans *= 2
        num = []
        while ans > 0:
            num.append(ans%10)
            ans = ans // 10
        num = num[::-1]
        ans = ListNode(0)
        dummy = ans
        for i in num:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans
        