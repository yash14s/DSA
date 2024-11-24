'''
https://leetcode.com/problems/maximum-product-of-three-numbers/description/
Logic math
'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        def bruteForce():
            #Too slow O(n3)
            maxProd = nums[0] * nums[1] * nums[2]
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        if i != j and j != k and k != i:
                            prod = nums[i] * nums[j] * nums[k]
                            if prod > maxProd:
                                maxProd = prod
            
            return maxProd


        def logic(nums):
            nums = sorted(nums)
            biggest = nums[-3:]
            smallest = nums[0:2]

            bigProd = biggest[0] * biggest[1]
            smallProd = smallest[0] * smallest[1]

            return max(smallProd*biggest[2], bigProd*biggest[2])


        return logic(nums)