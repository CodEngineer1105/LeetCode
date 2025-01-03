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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry =0;
        ListNode ans = l1;
        l1.val +=l2.val;
        carry = l1.val/10;
        l1.val %=10;
        while(l1.next!=null && l2.next!=null){
            l1.next.val +=l2.next.val+carry;
            carry = l1.next.val/10;
            l1.next.val %= 10;
            l1 = l1.next;
            l2 = l2.next;
        }
        if(l1.next==null){
            l1.next = l2.next;
        }
        while(l1.next!=null){
            l1.next.val += carry;
            carry = l1.next.val/10;
            l1.next.val %= 10;
            l1 = l1.next;
        }
        if(carry!=0){
            ListNode l = new ListNode(carry);
            l1.next = l;
        }
        return ans;
    }
}
