class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # If total '?' is odd, Alice always wins
        if (left_q + right_q) % 2:
            return True

        # Difference that Bob needs to cancel
        diff = left_sum - right_sum
        q_diff = left_q - right_q

        return diff * 2 != -9 * q_diff
