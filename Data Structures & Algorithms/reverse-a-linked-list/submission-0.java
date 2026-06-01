public class ListNodee{
    int val;

    ListNodee next;
    ListNodee(int x){
        val = x;
        next = null;
    }
} 
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null){
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}
