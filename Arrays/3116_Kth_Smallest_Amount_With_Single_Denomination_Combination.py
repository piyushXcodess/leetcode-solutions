class Solution:
    def findKthSmallest(self, coins, k):
        from math import gcd

        n = len(coins)

        # LCM of a set of coins
        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count how many valid amounts <= x
        def count(x):
            ans = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            valid = False
                            break

                if not valid:
                    continue

                ways = x // multiple

                if bits % 2:
                    ans += ways
                else:
                    ans -= ways

            return ans

        # Binary search for kth smallest
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
