class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_recursive(self, node):
        print("reverse_recursive(", node.value, ")")
        # Base case: if node is None or node is the last node
        if node is None or node.next is None:
            self.head = node
            return node
        
        # Recursively reverse the rest of the list
        reversed_list_head = self.reverse_recursive(node.next)

        print("reversed_list_head=",reversed_list_head.value)
        
        # Re-link the current node's next node back to the current node
        print("Re-linking line for node=", node.value)
        node.next.next = node
        node.next = None  # Set the next of current node to None
        
        return reversed_list_head

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.head.next = Node(2)
linked_list.head.next.next = Node(3)
linked_list.head.next.next.next = Node(4)

print("Original List:")
linked_list.print_list()

linked_list.reverse_recursive(linked_list.head)

print("Reversed List:")
linked_list.print_list()
