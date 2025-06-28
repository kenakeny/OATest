class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second = slow.next
        slow.next=None
        prev=None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next=temp1
            first,second=temp1,temp2
            #essentially we divide the ll into two halves n/2, we then reverse the second half and merge them