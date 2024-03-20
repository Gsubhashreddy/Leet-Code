/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        
        if(list1 == null || list2 == null) return list1;
        int count = 0;
        ListNode temp = list1;
        ListNode prev = null;
        ListNode nextVal = null;
        while(temp!=null){
            count++;
            if(count==a){
                prev = temp;
            }
            if(count == b+1){
                nextVal = temp;
                break;
            }
            temp = temp.next;
        }
        prev.next = list2;
        ListNode curr = list2;
        while(curr.next!=null){
            curr = curr.next;
        }
        curr.next = nextVal.next;
        return list1;
    }
}