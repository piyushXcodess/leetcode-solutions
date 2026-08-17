from bisect import bisect_left, bisect_right

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score Alice can get from l...r
        dp = [[0] * n for _ in range(n)]

        # left_best[l][r] =
        # max(dp[l][k] + prefix[k+1]) for l <= k <= r
        left_best = [[0] * n for _ in range(n)]

        # right_best[r][l] =
        # max(dp[k+1][r] - prefix[k+1]) for l <= k < r
        right_best = [[-10**18] * n for _ in range(n)]

        # Base case: one stone -> game ends, score = 0
        for i in range(n):
            left_best[i][i] = prefix[i + 1]

        # Process starting index from right to left
        for l in range(n - 1, -1, -1):

            # r increases
            for r in range(l + 1, n):

                total = prefix[r + 1] - prefix[l]

                # ------------------------------------------------
                # Build right_best[r][l]
                # ------------------------------------------------
                value = dp[l + 1][r] - prefix[l + 1]

                if l + 1 < r:
                    right_best[r][l] = max(
                        value,
                        right_best[r][l + 1]
                    )
                else:
                    right_best[r][l] = value

                # ------------------------------------------------
                # Find the split point
                # ------------------------------------------------
                #
                # left sum <= right sum
                #
                # prefix[k+1] - prefix[l] <= total / 2
                #
                limit = total // 2

                pos = bisect_right(
                    prefix,
                    prefix[l] + limit,
                    l + 1,
                    r + 1
                ) - 1

                best = 0

                # ------------------------------------------------
                # Case 1:
                # left side <= right side
                # Alice keeps left side
                # ------------------------------------------------
                if pos >= l + 1:
                    k = pos - 1

                    best = max(
                        best,
                        left_best[l][k] - prefix[l]
                    )

                # ------------------------------------------------
                # Case 2:
                # right side <= left side
                # Alice keeps right side
                # ------------------------------------------------
                need = prefix[l] + (total + 1) // 2

                pos2 = bisect_left(
                    prefix,
                    need,
                    l + 1,
                    r + 1
                )

                if pos2 <= r:
                    k = pos2 - 1

                    best = max(
                        best,
                        right_best[r][k] + prefix[r + 1]
                    )

                dp[l][r] = best

                # Update left_best
                current = dp[l][r] + prefix[r + 1]

                if r == l + 1:
                    left_best[l][r] = max(
                        left_best[l][l],
                        current
                    )
                else:
                    left_best[l][r] = max(
                        left_best[l][r - 1],
                        current
                    )

        return dp[0][n - 1]
