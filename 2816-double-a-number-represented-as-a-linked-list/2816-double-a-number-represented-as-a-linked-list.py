# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            return prev
        head = reverse(head)
        borrow = 0
        curr = head
        prev = None
        while curr:
            val = (curr.val * 2) + borrow
            if val > 9:
                borrow = 1
                val = val - 10
            else:
                borrow = 0
            curr.val = val
            prev = curr
            curr = curr.next
        curr = prev
        if borrow == 1:
            temp = ListNode(1)
            curr.next = temp
            curr = temp
        head = reverse(head)
        return head

        return None
        