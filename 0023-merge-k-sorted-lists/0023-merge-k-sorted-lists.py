# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        value = []
        for i in range(len(lists)):
            while lists[i] != None:
                value.append(lists[i].val)
                lists[i] = lists[i].next
        value.sort()
        ans = ListNode(0)
        dummy = ans
        for i in value:
            ans.next = ListNode(i)
            ans = ans.next
        ans = dummy.next
        return ans
        