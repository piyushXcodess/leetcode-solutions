class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Exactly k ones
            while ones == k:
                current = s[left:right + 1]

                # Shorter is better
                if ans == "" or len(current) < len(ans):
                    ans = current

                # Same length -> lexicographically smaller
                elif len(current) == len(ans) and current < ans:
                    ans = current

                if s[left] == '1':
                    ones -= 1

                left += 1

        return ans
