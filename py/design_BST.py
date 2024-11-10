'''
https://neetcode.io/problems/binarySearchTree
'''

class TreeMapNode:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val


class TreeMap:
    
    def __init__(self):
        self.root = None
        
    def insertRecursive(self, root, key, val):
        if not root:
            node = TreeMapNode(key, val)
            return node
        
        if key < root.key:
            root.left = self.insertRecursive(root.left, key, val)
        elif key > root.key:
            root.right = self.insertRecursive(root.right, key, val)
        else:
            root.val = val  
        return root


    def insert(self, key: int, val: int) -> None:
        if not self.root:
            node = TreeMapNode(key, val)
            self.root = node

        else:
            self.insertRecursive(self.root, key, val)
        

    def getRecursive(self, root, key):
        if not root:
            return -1
        else:
            if key < root.key:
                return self.getRecursive(root.left, key)
            elif key > root.key:
                return self.getRecursive(root.right, key)
            else:
                return root.val


    def get(self, key: int) -> int:
        return self.getRecursive(self.root, key)


    def getMinRecursive(self, root):
        if not root.left:
            return root.val
        
        return self.getMinRecursive(root.left)


    def getMin(self) -> int:
        if not self.root:
            return -1

        return self.getMinRecursive(self.root)


    def getMaxRecursive(self, root):
        if not root.right:
            return root.val
        
        return self.getMaxRecursive(root.right)


    def getMax(self) -> int:
        if not self.root:
            return -1
            
        return self.getMaxRecursive(self.root)


    def findMinKeyNode(self, root):
        if not root.left:
            return root
        return self.findMinKeyNode(root.left)


    def removeRecursive(self, root, key):
        if not root:
            return None

        if key < root.key:
            root.left = self.removeRecursive(root.left, key)
        elif key > root.key:
            root.right = self.removeRecursive(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minKeyNode = self.findMinKeyNode(root.right)
                root.key = minKeyNode.key
                root.val = minKeyNode.val
                root.right = self.removeRecursive(root.right, minKeyNode.key)

        return root


    def remove(self, key: int) -> None:
        self.root = self.removeRecursive(self.root, key)

    def inorderRecursive(self, root):
        if not root:
            return []
        left = self.inorderRecursive(root.left)
        curr = root.key
        right = self.inorderRecursive(root.right)
        return left + [root.key] + right


    def getInorderKeys(self) -> List[int]:
        return self.inorderRecursive(self.root)