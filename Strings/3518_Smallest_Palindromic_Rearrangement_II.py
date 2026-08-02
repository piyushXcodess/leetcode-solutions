"""
LeetCode 3518 - Smallest Palindromic Rearrangement II

Difficulty: Hard
Topic: Strings, Combinatorics

Language: Python
"""
from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = []
        mid = ""

        for ch in sorted(cnt):
            if cnt[ch] & 1:
                mid = ch
            half.extend([ch] * (cnt[ch] // 2))

        freq = Counter(half)

        LIMIT = 10 ** 6

        def count_perm(freq):
            total = sum(freq.values())
            res = 1
            rem = total
            for c in freq.values():
                if c:
                    res *= comb(rem, c)
                    if res > LIMIT:
                        return LIMIT + 1
                    rem -= c
            return res

        if count_perm(freq) < k:
            return ""

        left = []

        while sum(freq.values()):
            for ch in sorted(freq):
                if freq[ch] == 0:
                    continue

                freq[ch] -= 1
                ways = count_perm(freq)

                if ways >= k:
                    left.append(ch)
                    break
                else:
                    k -= ways
                    freq[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]
