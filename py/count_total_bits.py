'''
https://leetcode.com/problems/counting-bits/
Bit manipulation
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        cache = {}  #memoization for efficiency.
        numBits = []

        for i in range(n+1):
            j = i
            bits = 0
            while i > 0:
                if i in cache:
                    bits += cache[i]
                    break
                if i & 1 == 1:
                    bits += 1
                i = i >> 1
            numBits.append(bits)
            if j not in cache:
                cache[j] = bits

        return numBits