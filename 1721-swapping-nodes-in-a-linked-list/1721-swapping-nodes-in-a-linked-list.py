# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        num = []
        while head != None:
            num.append(head.val)
            head = head.next
        temp = num[k-1]
        num[k-1] = num[len(num) - k]
        num[len(num) - k] = temp
        ans = ListNode(0)
        dummy = ans
        for i in num:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans
        