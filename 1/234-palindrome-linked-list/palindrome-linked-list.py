# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        f = head
        s = head

        while f and f.next:
            f = f.next.next
            s = s.next
        

        prev = None

        while s:
            nxt = s.next
            s.next = prev
            prev = s
            s = nxt
        
        left = head
        right = prev

        while right:
            if left.val!=right.val:
                return False
            
            left=left.next
            right=right.next
        
        return True
            
            