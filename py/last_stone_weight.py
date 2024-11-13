'''
https://leetcode.com/problems/last-stone-weight/
Simple heap ops
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash(x,y):
            return y-x

        maxHeap = [-x for x in stones]
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -1 * heapq.heappop(maxHeap)
            x = -1 * heapq.heappop(maxHeap)

            diff = smash(x,y)

            if diff > 0:
                heapq.heappush(maxHeap, -diff)
        
        if len(maxHeap) > 0:
            return -1 * heapq.heappop(maxHeap)
        return 0
