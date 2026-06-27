# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    # Solution to question 61
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or k == 0:
            return head
        
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        
        tail.next = head

        k = k % n
        steps = n - k

        newTail = head

        for i in range(steps - 1):
            newTail = newTail.next
        
        newhead = newTail.next
        newTail.next = None
        
        return newhead