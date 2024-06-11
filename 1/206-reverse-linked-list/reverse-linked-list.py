# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head 
        tail = None

        while curr:
            temp = tail 
            tail = curr
            curr = curr.next

            tail.next = temp

        head = tail
        return head
        