class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # suf[i] = word1[i:] ko use karke
        # word2 ka kitna suffix exactly match ho sakta hai
        suf = [0] * (n + 1)

        suf[n] = m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suf[i] = j + 1

        ans = []

        j = 0
        changed = False

        for i in range(n):

            if j == m:
                return ans

            # Normal exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

                if j == m:
                    return ans

            # Current character ko mismatch ke liye use kar sakte hain
            elif not changed and suf[i + 1] <= j + 1:
                changed = True
                ans.append(i)
                j += 1

                if j == m:
                    return ans

        return []
