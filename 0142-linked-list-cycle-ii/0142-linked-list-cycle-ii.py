# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head != None:
            if head in ans:
                num = ListNode(ans.index(head))
                return head
            ans.append(head)
            head = head.next
        
        