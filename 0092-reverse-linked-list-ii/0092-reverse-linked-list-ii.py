# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next==None:
            return head
        if left==right:
            return head
        #Now we have atleast 2 nodes
        i=1
        #Handle Base Case which is left==0
        prev=None
        curr=head
        fast=head.next
        while i<left and curr!=None:
            prev=curr
            curr=fast
            fast=fast.next
            i+=1
        MainHead=curr
        stPrev= prev
        # We have  Now prev and Curr Pointer
        # Proceed Till we get fast
        while left<right and fast!=None:
            curr.next=prev
            prev=curr
            curr=fast
            fast=fast.next
            left+=1
        if left==right:
            MainHead.next=curr.next
            curr.next=prev
            if stPrev:
                stPrev.next=curr
            else:
                head=curr
        return head



        