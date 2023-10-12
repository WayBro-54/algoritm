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
    
# print(Solution().increasingTriplet([2,1,5,0,4,6]))

# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        i = 0
        c = 0
        while i <= len(chars):
            x = chars[i]
            while x == chars[i+1]:
                i += 1
            # res.append(chars[i])
            # res.append(c)

        return res


# print(Solution().compress(["a","a","b","b","c","c","c"]))


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)
        return nums

# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0
        c_s = len(s)
        c_t = len(t)

        while i < c_s and j < c_t:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == j


# print(Solution().isSubsequence(s = 'abc', t = 'ahbgdc'))


# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = set()
        for i, value in enumerate(height):
            for j in range(i, len(height)):
                res.add((j-i) * min([value, height[j]]) )
        return max(res)

# print(Solution().maxArea(x))


# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # for i, value in enumerate(s):
        sogl = 'aeuio'
        c = 0
        curr = float('-inf')
        curr_list = [i for i, value in enumerate(s) if value in sogl]
        for i in range(len(curr_list)):
            l = curr_list[i] + k
            for j in range(i, len(curr_list)):
                if l > curr_list[j]:
                    c += 1

        return c

# print(Solution().maxVowels('weallloveyou', 7))
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res_summ = 0
        i = 0
        # curr_summ = 0

        while i < len(cost) - 1:
            res_summ += min(cost[i], cost[i + 1])
            print(i, res_summ)
            if cost[i] == cost[i + 1]:
                i += 1
            i += 1
        return res_summ

# print(Solution().minCostClimbingStairs([10, 15,20 ]))


# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height, curr = 0, 0

        for i in gain:
            curr += i
            max_height = max(max_height, curr)
        return max_height

from time import sleep
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = sum(nums)

        for i in range(len(nums)):
            rSum -= nums[i]
            if lSum == rSum:
                return i
            lSum += nums[i]

        return -1

print(Solution().pivotIndex([-1,-1,-1,-1,-1,-1]))
