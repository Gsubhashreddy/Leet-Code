# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            curr = head
            while curr!= None:
                ne = curr.next
                curr.next = prev
                prev = curr
                curr = ne
            return prev
        
        head = reverse(head)
        curr = head
        small = 0
        prev = None
        while curr!=None:
            if curr.val>= small:
                small = curr.val
                if prev:
                    prev.next = curr
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        # print(head.next.val)
                # # 8-> 3 -> 13 - 2 - 5
                # p = 8, c = 3
        head = reverse(head)
        return head