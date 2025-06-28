class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast= head,head
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        #my intuition was to do a hashMap and see if the node already existed
        #fast and slow pointers are very interesting tho 