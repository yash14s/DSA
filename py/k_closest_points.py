'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compute_distance(point):
            return (point[0]**2 + point[1]**2)**0.5
        
        heap = [{tuple(point):compute_distance(point)} for point in points]
        heap = self.heapify(heap)

        res = []
        for i in range(k):
            res.append(list(next(iter(self.heap_pop(heap).keys()))))
        
        return res
    
    def percolate_down(self, heap, i):
        while 2*i < len(heap):
            if 2*i+1 < len(heap) and next(iter(heap[2*i+1].values())) < next(iter(heap[2*i].values())) and next(iter(heap[2*i+1].values())) < next(iter(heap[i].values())):
                tmp = heap[2*i+1]
                heap[2*i+1] = heap[i]
                heap[i] = tmp
                i = 2*i+1
            elif next(iter(heap[2*i].values())) < next(iter(heap[i].values())):
                tmp = heap[2*i]
                heap[2*i] = heap[i]
                heap[i] = tmp
                i = 2*i
            else:
                break

    def heapify(self, arr):
        heap = [0] + arr
        
        curr = (len(heap)-1)//2
        while curr > 0:
            i = curr
            self.percolate_down(heap, i)
            curr -= 1
        return heap

    def heap_pop(self, heap):
        val = heap[1]
        heap[1] = heap[-1]
        heap.pop()
        self.percolate_down(heap, 1)
        return val
