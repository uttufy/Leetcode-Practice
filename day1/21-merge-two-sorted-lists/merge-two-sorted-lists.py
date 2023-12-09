# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1 and list2 is None:
        #     return None
            
        if list1 is None:
            return list2 # return head
        
        if list2 is None:
            return list1

        head = ListNode()
        curr = head

        while list1!=None and list2!=None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
            
        curr.next = list1 or list2

        return head.next

        