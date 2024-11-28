# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#Recursion
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

#Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return
            
        prev = head
        curr = head
        next = head

        while curr.next:
            next = curr.next
            if curr == head:
                curr.next = None
            else:
                curr.next = prev
            prev = curr
            curr = next
        
        if curr == head:
            return head
        
        curr.next = prev
        head = curr
        return head