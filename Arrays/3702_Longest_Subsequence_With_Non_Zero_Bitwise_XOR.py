class Solution:
    def longestSubsequence(self, nums):
        xor = 0

        for x in nums:
            xor ^= x

        if xor != 0:
            return len(nums)

        for x in nums:
            if x != 0:
                return len(nums) - 1

        return 0
