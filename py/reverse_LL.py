'''
Reverse a LL using recursion
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        if node is None or node.next is None:
            head = node
            return head
        
        reverse = self.reverseList(node.next)

        node.next.next = node
        node.next = None

        return reverse
