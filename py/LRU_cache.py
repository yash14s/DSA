'''
https://leetcode.com/problems/lru-cache/
System design
DLL, Hashmaps, Edge-case handling
'''

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    def __init__(self) -> None:
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU


class LRUCache:

    def __init__(self, capacity: int):
        self.hashMapLL = DLL()
        self.cap = capacity
        self.size = 0
        self.hashMap = {}    

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        curr = self.hashMap[key]
        val = curr.val
        self.removeNode(curr)
        self.updateMRU(curr)
        return val
    
    def add(self, key, val):
        self.hashMap[key] = Node(key,val)
        self.size += 1
        if self.size == 1:
            curr = self.hashMap[key]
            prev = self.hashMapLL.LRU
            next = self.hashMapLL.MRU
            prev.next = curr
            next.prev = curr
            curr.prev = prev
            curr.next = next

    def removeNode(self, node):
        curr = node
        prev = curr.prev
        next = curr.next
        next.prev = prev
        prev.next = next
        curr.prev = None
        curr.next = None

    def removeLRU(self):
        curr = self.hashMapLL.LRU.next
        key = curr.key
        self.removeNode(curr)
        self.hashMap.pop(key)
        self.size -= 1
    
    def updateMRU(self, node):
        curr = node
        prev = self.hashMapLL.MRU.prev
        if prev == curr:
            return
        next = self.hashMapLL.MRU
        prev.next = curr    
        next.prev = curr
        curr.prev = prev
        curr.next = next

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            curr = self.hashMap[key]
            curr.val = value
            if self.hashMapLL.MRU.prev == curr:
                return
            #update position
            self.removeNode(curr)
            self.updateMRU(curr)
        
        else:
            if self.size < self.cap:
                self.add(key, value)
                curr = self.hashMap[key]
                self.updateMRU(curr)
            
            else:
                #remove LRU
                self.removeLRU()
                #insert
                self.add(key, value)
                #move to MRU
                curr = self.hashMap[key]
                self.updateMRU(curr)
