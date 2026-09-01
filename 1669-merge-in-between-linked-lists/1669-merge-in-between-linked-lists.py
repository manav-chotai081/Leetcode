# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        num1 = []
        while list1 != None:
            num1.append(list1.val)
            list1 = list1.next
        ans = ListNode(0)
        dummy = ans
        for i in range(a):
            ans.next = ListNode(num1[i])
            ans = ans.next
        while list2 != None:
            ans.next = ListNode(list2.val)
            ans = ans.next
            list2 = list2.next
        for i in range(b+1,len(num1)):
            ans.next = ListNode(num1[i])
            ans = ans.next
        ans = dummy.next
        return ans