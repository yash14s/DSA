'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = curr = 0
        while curr < len(nums):
            if nums[curr] == nums[dup]:
                curr += 1
            else:
                dup += 1
                nums[dup] = nums[curr]
        
        return dup + 1