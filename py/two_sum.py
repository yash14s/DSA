'''
https://leetcode.com/problems/two-sum/
Using hash maps, an solve it in O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        #brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
        '''

        #using hash map
        valMap = {}

        for i in range(len(nums)):
            valMap[nums[i]] = i
        
        complements = [target-num for num in nums]

        for i in range(len(complements)):
            c = complements[i]
            if c in valMap and i != valMap[c]:
                return [valMap[c], i]