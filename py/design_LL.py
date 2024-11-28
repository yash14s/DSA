class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
        self.head = None
        self.tail = None


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val
        
        
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)

        if not self.head:
            next = self.right
            prev = self.left
            self.tail = node
        else:
            next = self.head
            prev = self.left
            
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node

        self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        if not self.tail:
            self.addAtHead(val)
            return
        else:
            next = self.right
            prev = self.tail
            
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node

        self.tail = node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return -1

        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return

        node = ListNode(val)
        curr = self.head
        for _ in range(index):
            curr = curr.next
        next = curr
        prev = curr.prev
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node
        self.size += 1

        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        next = curr.next
        prev = curr.prev
        prev.next = next
        next.prev = prev

        if index == 0:
            self.head = next
        elif index == self.size-1:
            self.tail = prev

        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)