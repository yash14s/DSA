class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k

        for i in range(len(nums)):
            self.push(nums[i])
        print(self.heap)

        #only keep top k elements
        while len(self.heap) > self.k + 1:
            self.pop()
        print(self.heap)

    def push(self, val):
        if len(self.heap) == 1:
            self.heap.append(val)
            return
        # Add to the end and percolate up
        self.heap.append(val)
        i = len(self.heap) - 1
        curr = self.heap[i]
        parent = self.heap[i//2]
        
        while curr < parent and i > 0:
            tmp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = tmp
            i //= 2
            curr = self.heap[i]
            parent = self.heap[i//2]
    

    def pop(self):
        '''
        pop the root
        '''
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        #percolate down
        i = 1
        curr = i
        left_child = 2 * i
        right_child = (2 * i) +  1

        while i < len(self.heap) and left_child < len(self.heap):
            if right_child < len(self.heap):
                if (self.heap[curr] > self.heap[left_child] or self.heap[curr] > self.heap[left_child]):
                    if self.heap[left_child] < self.heap[right_child]:
                        tmp = self.heap[left_child]
                        self.heap[left_child] = self.heap[curr]
                        self.heap[curr] = tmp
                        i = left_child
                    else:
                        tmp = self.heap[right_child]
                        self.heap[right_child] = self.heap[curr]
                        self.heap[curr] = tmp
                        i = right_child
                    
                    curr = i
                    left_child = 2 * i
                    right_child = (2 * i) +  1
            
            elif self.heap[curr] > self.heap[left_child]:
                tmp = self.heap[left_child]
                self.heap[left_child] = self.heap[curr]
                self.heap[curr] = tmp
                i = left_child
                curr = i
                left_child = 2 * i
                right_child = (2 * i) +  1
            
            else:
                break


    def add(self, val: int) -> int:
        self.push(val)
        print(self.heap)
        return self.heap[-self.k]
