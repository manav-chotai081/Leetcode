# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
        ans = ListNode(0)
        dummy = ans
        for i in range(0,len(value),2):
            ans.next = ListNode(value[i])
            ans = ans.next
        for i in range(1,len(value),2):
            ans.next = ListNode(value[i])
            ans = ans.next
        ans = dummy.next
        return ans
        