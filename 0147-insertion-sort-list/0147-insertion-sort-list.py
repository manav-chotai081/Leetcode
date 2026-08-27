# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
        value.sort()
        ans = ListNode(0)
        dummy = ans
        for i in value:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans
        