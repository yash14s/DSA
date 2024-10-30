'''
https://neetcode.io/problems/merge-k-sorted-linked-lists

Recursion, Inspired by MergeSort logic
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge cases
        if lists == [] or lists == [[]] or lists is None:
            return None
        
        #base case
        if len(lists) == 1:
            return lists[0]

        head = ListNode()
        curr = head
        left = lists[0]
        right = lists[1]

        curr1 = left
        curr2 = right

        while curr1 is not None and curr2 is not None:
            node = ListNode()

            if curr1.val <= curr2.val:
                node.val = curr1.val
                curr1 = curr1.next
            else:
                node.val = curr2.val
                curr2 = curr2.next
            
            curr.next = node
            curr = curr.next

        if curr1 is not None:
            curr.next = curr1
        else:
            curr.next = curr2

        head = head.next #this is the merged LL for left and right
        lists[0] = head
        del lists[1]

        self.mergeKLists(lists) #recursive call

        return lists[0]
