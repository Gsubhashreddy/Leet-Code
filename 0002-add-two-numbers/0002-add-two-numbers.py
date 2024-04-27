# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        su = l1.val + l2.val
        bo = 0
        if su > 9:
            bo = 1
            res = ListNode(su - 10)
        else:
            res = ListNode(su)
            bo = 0
        temp = res
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            su = l1.val + l2.val + bo
            if su > 9:
                bo = 1
                tmp = ListNode(su - 10)
            else:
                tmp = ListNode(su)
                bo = 0
            temp.next = tmp
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        if l2:
            l1 = l2      
        while l1:
            su = l1.val + bo
            if su > 9:
                bo = 1
                tmp = ListNode(su - 10)
            else:
                tmp = ListNode(su)
                bo = 0
            temp.next = tmp
            temp = temp.next
            l1 = l1.next
        if bo != 0:
            tmp = ListNode(1)
            temp.next = tmp
        return res
                
            
        