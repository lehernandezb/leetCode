# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        
        if length == n:
            return head.next 
        
        remove = length - n - 1

        prev = head
        while remove > 0:
            prev = prev.next
            remove -= 1

        prev.next = prev.next.next
        return head