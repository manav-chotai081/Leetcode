# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # newNode =ListNode(0)
#         # data = newNode.next
#         # return data

#         # data = l1.next
#         # return data
#         num1 = 0 
#         while l1 != None:
#             num1 *= 10
#             num1 += l1.val
#             l1 = l1.next
#         num2 = 0
#         while l2 != None:
#             num2 *= 10
#             num2 += l2.val
#             l2 = l2.next
#         num = str(num1)
#         num1 = int(num[::-1])
#         num = str(num2)
#         num2 = int(num[::-1])
#         ans = num1 + num2
#         if ans == 0:
#             new = ListNode(ans)
#             return new
#         dummy = ListNode(0)
#         ans1 = dummy
#         while ans > 0:
#             ans1.next = ListNode(ans%10)
#             ans = ans // 10
#             ans1 = ans1.next
#         ans1 = dummy.next
#         return ans1

            

            
        

            
        





class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        while l1 != None:
            num1.append(l1.val)
            l1 = l1.next
        num1 = num1[::-1]
        num2 = []
        while l2 != None:
            num2.append(l2.val)
            l2 = l2.next
        num2 = num2[::-1]
        carry = 0
        ans1 = 0
        for i in num1:
            ans1 *= 10
            ans1 += i
        ans2 = 0
        for i in num2:
            ans2 *= 10
            ans2 += i

        num = ans1 + ans2
        if num == 0:
            return ListNode(0)
        ans = ListNode(0)
        dummy = ans
        while num > 0:
            ans.next = ListNode(num%10)
            num = num // 10
            ans = ans.next
        ans = dummy.next
        return ans
        
        