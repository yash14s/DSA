class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k

        for i in range(len(nums)):
            self.push(nums[i])

    
    def push(self, val):
        if len(self.heap) == 1:
            self.heap.append(val)
            return
        # Add to the end and percolate up
        self.heap.append(val)
        i = len(self.heap) - 1
        curr = self.heap[i]
        parent = self.heap[i//2]
        
        while curr < parent and i > 1:
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

        while 2 * i < len(self.heap):
            if (2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i+1]):
                tmp = self.heap[2*i+1]
                self.heap[2*i+1] = self.heap[i]
                self.heap[i] = tmp
                i = 2*i+1

            elif self.heap[i] > self.heap[2*i]:
                tmp = self.heap[2*i]
                self.heap[2*i] = self.heap[i]
                self.heap[i] = tmp
                i = 2*i

            else:
                break


    def add(self, val: int) -> int: 
        self.push(val)
        while len(self.heap) > self.k + 1:
            self.pop()
        
        return self.heap[-self.k]
