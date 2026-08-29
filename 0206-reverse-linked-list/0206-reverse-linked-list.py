# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head != None:
            ans.append(head.val)
            head = head.next
        ans = ans[::-1]
        ans1 = ListNode(0)
        dummy = ans1
        for i in ans:
            ans1.next = ListNode(i)
            ans1 = ans1.next
        ans1 = dummy.next
        return ans1
        