# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        dummyNode = ListNode()
        currNode = head
        prevNode = dummyNode

        while currNode and currNode.next is not None:
           prevNode.next = currNode.next
           currNode.next = prevNode.next.next
           prevNode.next.next = currNode

           prevNode = currNode
           currNode = currNode.next

        return dummyNode.next