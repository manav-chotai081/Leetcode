# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans1 = []
        while head != None:
            ans1.append(head.val)
            head = head.next
        len1 = len(ans1)
        if len1 == 0:
            return None
        middle = len1 // 2
        ans = ListNode(0)
        dummy = ans
        for i in range(middle,len1):
            ans.next = ListNode(ans1[i])
            ans = ans.next
        ans = dummy.next
        return ans
        