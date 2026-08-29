# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans1 = []
        while head != None:
            ans1.append(head.val)
            head = head.next
        ans1.sort()
        ans = ListNode(0)
        dummy = ans
        for i in ans1:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans
        