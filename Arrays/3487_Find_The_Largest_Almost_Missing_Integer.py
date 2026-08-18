class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}

        # Har size-k window me number ko sirf ek baar count karo
        for i in range(n - k + 1):
            seen = set(nums[i:i + k])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x, c in count.items():
            if c == 1:
                ans = max(ans, x)

        return ans
