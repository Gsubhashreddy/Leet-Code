# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to simplify edge cases
        dummy.next = head
        first = dummy  # Start first at dummy node
        second = dummy  # Start second at dummy node

        # Advance second n + 1 times to create a gap of n between first and second
        for _ in range(n + 1):
            second = second.next

        # Move first and second at the same pace until second reaches the end
        while second:
            first = first.next
            second = second.next

        # Remove the Nth node from end
        first.next = first.next.next

        # Return head of the modified list, which might be different if the head was removed
        return dummy.next
            
        