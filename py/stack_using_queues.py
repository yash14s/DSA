'''
https://leetcode.com/problems/implement-stack-using-queues/

Used Linked List for Queue implementation
'''

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Queue:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.head = None
        self.tail = None
        self.size = 0

    def peek(self):
        return self.head.val
    
    def enqueue(self, val):
        node = Node(val)

        if self.size == 0:
            self.left.next = node
            node.next = self.right
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.next = self.right
            self.tail = node

        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return

        if self.size == 1:
            self.left.next = self.right
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.left.next = self.head
        
        self.size -= 1

    def is_empty(self):
        if self.size == 0:
            return True
        return False



class MyStack:

    def __init__(self):
        self.q = Queue()
        

    def push(self, x: int) -> None:
        self.q.enqueue(x)
        size = self.q.size

        iters = 0
        while iters < size - 1:
            val = self.pop()
            self.q.enqueue(val)
            iters += 1

        

    def pop(self) -> int:
        val = self.top()
        self.q.dequeue()

        return val
        

    def top(self) -> int:
        return self.q.peek()
        

    def empty(self) -> bool:
        return self.q.is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()