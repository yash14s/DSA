'''
https://neetcode.io/problems/eating-bananas
'''

class Solution:

    def compute_time_taken(self, piles, k):
        n = len(piles)
        times = [0] * n

        for i in range(n):
            times[i] = piles[i] // k
            rem = piles[i] % k
            if rem != 0:
                times[i] += 1

        return sum(times)


    def is_k_valid(self, piles, h, k):
        if self.compute_time_taken(piles, k) <= h:
            return True
        return False


    def compute_k_recursive(self, piles, l, r, h):
        if l > r:
            return l
        
        k = (l+r)//2
        
        if self.is_k_valid(piles, h, k):
            return self.compute_k_recursive(piles, l, k-1, h)
        else:
            return self.compute_k_recursive(piles, k+1, r, h)


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        return self.compute_k_recursive(piles, l, r, h)