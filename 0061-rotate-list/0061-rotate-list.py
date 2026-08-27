# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
        if len(value) == 0:
            head = None
            return head
        k = k % len(value)
        for i in range(k):
            value.insert(0, value[len(value)-1])
            value.pop()
        dummy = ListNode(0)
        ans = dummy
        for i in value:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans


        