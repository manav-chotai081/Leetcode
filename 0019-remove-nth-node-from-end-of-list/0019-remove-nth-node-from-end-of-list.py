# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
        len1 = len(value) - n
        value.pop(len1)
        ans = ListNode(0)
        dummy = ans
        for i in value:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans


        
        