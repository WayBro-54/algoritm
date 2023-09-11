# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            curr = target - value
            if curr in nums and nums.index(curr) != i:
                return [i, nums.index(curr)]

# x = Solution().twoSum([3, 2, 3], 6)
# print(x)

# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)
        return ''.join([i+j for i, j in zip(word1, word2)]) + word1[len_w2:] if len(word1) > len(word2) else ''.join([i+j for i, j in zip(word1, word2)]) + word2[len_w1:]
        # return

# print(Solution().mergeAlternately(word1 = "ab", word2 = "pqrs"))

# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

import functools
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        larger_counts = [0] * n
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    larger_counts[i] += 1
        return larger_counts
    
# print(Solution().productExceptSelf([1,2,3,4]))
x = [1,2,3,4]
# print(x[0:][1:])


# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

        
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        c = 1
        curr = nums[0]
        for i in nums[1:]:
            # print(curr)
            if curr < i:
                c += 1
                curr = i
            if c == 3:
                return True
        return False
    
print(Solution().increasingTriplet([2,1,5,0,4,6]))