# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # arr1 = []
        # while l1 != None:
        #     arr1.append(l1.val)
        #     l1 = l1.next
        # arr2 = []
        # while l2 != None:
        #     arr2.append(l2.val)
        #     l2 = l2.next
        
        arr = []
        while l1 != None:
            arr.append(l1.val)
            l1 = l1.next
        while l2 != None:
            arr.append(l2.val)
            l2 = l2.next
        arr.sort()

        ans = ListNode(0)
        dummy = ans
        for i in arr:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans
        