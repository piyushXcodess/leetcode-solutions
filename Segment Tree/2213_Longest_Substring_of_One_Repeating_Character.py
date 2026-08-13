class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices):
        n = len(s)

        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b

            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            length = a[5] + b[5]

            prefix = a[2]
            suffix = b[3]

            best = max(a[4], b[4])

            # Boundary characters are same
            if a[1] == b[0]:

                # Entire left segment has same character
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # Entire right segment has same character
                if b[3] == b[5]:
                    suffix = b[5] + a[3]

                # Run crossing the boundary
                best = max(best, a[3] + b[2])

            return [
                left_char,
                right_char,
                prefix,
                suffix,
                best,
                length
            ]

        def build(node, left, right):
            if left == right:
                tree[node] = [
                    s[left],   # left char
                    s[left],   # right char
                    1,         # prefix
                    1,         # suffix
                    1,         # best
                    1          # length
                ]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, idx, ch):
            if left == right:
                tree[node] = [
                    ch,
                    ch,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (left + right) // 2

            if idx <= mid:
                update(node * 2, left, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, right, idx, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans
