# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        daddy = ListNode(0,head)
        left=daddy
        right=head
        while n>0:
            right=right.next
            n-=1 #essentially we make
        while right:
            left= left.next
            right=right.next
        left.next=left.next.next
        return daddy.next

#essentially u do n moves from the start to move the right pointer
#then u move hte 