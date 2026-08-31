# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        value = []
        while head != None:
            value.append(head.val)
            head = head.next
        temp = 0
        while temp < len(value):
            if temp+k<= len(value):
                value[temp:temp+k] = value[temp:temp+k][::-1]
            temp += k
        ans = ListNode(0)
        dummy = ans
        for i in value:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans



        