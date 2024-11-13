'''
Implementing minheap from scratch
https://neetcode.io/problems/heap
'''
class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:   
        self.heap.append(val)
        i = len(self.heap) - 1

        #percolate up
        while self.heap[i//2] > self.heap[i] and i > 1:
            tmp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = tmp
            i = i//2


    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        
        min_val = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        #percolate down
        i = 1

        while 2 * i < len(self.heap):
            if 2*i+1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[2*i+1] < self.heap[i]:
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
        
        return min_val


    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        
        return -1
        

    def heapify(self, nums: List[int]) -> None:
        if len(nums) == 0:
            self.heap = [0]
            return
        #structure property
        nums.append(nums[0])
        nums[0] = 0

        #order property
        curr = (len(nums)-1)//2
    
        while curr > 0:
            i = curr
            while 2*i < len(nums):
                if 2*i+1 < len(nums) and nums[2*i+1] < nums[2*i] and nums[2*i+1] < nums[i]:
                    tmp = nums[2*i+1]
                    nums[2*i+1] = nums[i]
                    nums[i] = tmp
                    i = 2*i+1
                elif nums[i] > nums[2*i]:
                    tmp = nums[2*i]
                    nums[2*i] = nums[i]
                    nums[i] = tmp
                    i = 2*i
                else:
                    break
            curr -= 1
        
        self.heap = nums