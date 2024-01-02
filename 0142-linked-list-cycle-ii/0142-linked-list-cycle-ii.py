# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        slow,fast=head,head
        slow=slow.next
        fast=fast.next.next
        while(fast!=None and fast.next!=None):
            if slow==fast:
                break
            slow=slow.next
            fast=fast.next.next
        if slow!=fast:
            return None
        slow=head
        while(slow!=fast):
            slow=slow.next
            fast=fast.next
        return slow
        