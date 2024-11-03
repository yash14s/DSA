'''
https://leetcode.com/problems/sort-colors/

Bucket Sort since number of colors is finite (3)
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]

        for i in range(len(nums)):
            n = nums[i]
            counts[n] += 1
        
        i = 0
        n = 0

        while i < len(nums) and n < len(counts):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
            n += 1

        return nums 