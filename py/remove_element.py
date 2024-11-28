'''
https://leetcode.com/problems/remove-element/
Array 2 pointer technique
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        for slow in range(n-1, -1, -1):
            if nums[slow] != val:
                break
        
        if slow == 0 and nums[0] == val:
            return 0

        fast = 0

        while fast < slow:
            if nums[fast] == val:
                nums[fast] = nums[slow]
                slow -= 1

                while slow > fast and nums[slow] == val:
                    slow -= 1
            
            fast += 1
        
        return slow + 1