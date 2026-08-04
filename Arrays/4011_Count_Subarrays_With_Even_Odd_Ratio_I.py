"""
LeetCode 4011 - Count Subarrays With Even Odd Ratio I

Difficulty: Medium
Category: Arrays

Approach:
- Brute Force
- Count even and odd elements for every subarray.
- Check whether the ratio of even to odd elements is <= a / b.

Time Complexity: O(n²)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            even = 0
            odd = 0

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even += 1
                else:
                    odd += 1

                if odd > 0 and even * b <= odd * a:
                    ans += 1

        return ans
