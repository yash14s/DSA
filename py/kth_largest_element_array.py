'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        for i in range(k-1):
            heapq.heappop(heap)
        
        return -1*heapq.heappop(heap)
