# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans1 = []
        while head != None:
            ans1.append(head.val)
            head = head.next
        if ans1 == ans1[::-1]:
            return True
        return False

        