# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        ans = []
        ind = []
        count = 0
        while head != None:
            ans.append(head.val)
            if head.val == 0:
                ind.append(count)
            head = head.next
            count += 1
        ans1 = []
        for i in range(len(ind)-1):
            first = ind[i]
            second = ind[i+1]
            ans1.append(sum(ans[first:second]))
        l1 = ListNode(0)
        dummy = l1
        for i in ans1:
            l1.next = ListNode(i)
            l1 = l1.next
        l1 = dummy.next
        return l1

        