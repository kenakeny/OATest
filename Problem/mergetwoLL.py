# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        aamo=node1=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                node1.next=list1
                list1=list1.next
            else:
                node1.next=list2
                list2=list2.next
            node1=node1.next
        node1.next=list1 or list2 #incase one of them ended
        return aamo.next
        #this was pretty easy