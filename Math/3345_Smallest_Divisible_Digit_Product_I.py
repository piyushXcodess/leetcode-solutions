"""
LeetCode 3345 - Smallest Divisible Digit Product I
Difficulty: Easy
Topic: Math, Brute Force

Time Complexity: O(k × d)
Space Complexity: O(1)
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def digitProduct(x):
            product = 1
            while x > 0:
                product *= x % 10
                x //= 10
            return product

        while True:
            if digitProduct(n) % t == 0:
                return n
            n += 1
