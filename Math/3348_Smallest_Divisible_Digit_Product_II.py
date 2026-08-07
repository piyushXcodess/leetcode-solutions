import sys
from functools import lru_cache

# Safely raise recursion limit for our DP (though maximum depth is extremely small now)
sys.setrecursionlimit(2000)

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Count prime factors of t
        temp = t
        counts = [0, 0, 0, 0] # mapping to prime counts for: 2, 3, 5, 7
        primes = [2, 3, 5, 7]
        for i, p in enumerate(primes):
            while temp % p == 0:
                counts[i] += 1
                temp //= p
        
        # If t has any prime factors outside of 2, 3, 5, 7, it's impossible to form with digits 1-9
        if temp > 1:
            return "-1"
            
        # DP to find minimum digits needed to satisfy required factors of 2 and 3
        @lru_cache(None)
        def min_digits_23(a, b):
            # Base case: All requirements met
            if a <= 0 and b <= 0:
                return 0
            
            # Clamp negative requirements to 0 so we don't over-track
            a = max(0, a)
            b = max(0, b)
            
            res = float('inf')
            
            # Only attempt to use factors of 2 if we actually need them
            if a > 0:
                res = min(res, 1 + min_digits_23(a - 3, b))                # Use digit 8
                res = min(res, 1 + min_digits_23(a - 2, b))                # Use digit 4
                res = min(res, 1 + min_digits_23(a - 1, b))                # Use digit 2
                
            # Only attempt to use factors of 3 if we actually need them
            if b > 0:
                res = min(res, 1 + min_digits_23(a, b - 2))                # Use digit 9
                res = min(res, 1 + min_digits_23(a, b - 1))                # Use digit 3
                
            # Only attempt digit 6 if we need BOTH factors
            if a > 0 and b > 0:
                res = min(res, 1 + min_digits_23(a - 1, b - 1))            # Use digit 6
                
            return res
            
        def get_min_len(req):
            c2, c3, c5, c7 = req
            # Digits 5 and 7 are primes, they mandate independent digits
            return max(0, c5) + max(0, c7) + min_digits_23(max(0, c2), max(0, c3))

        # (Count of 2s, 3s, 5s, 7s) provided by each digit index 0-9
        DIGIT_FACTORS = [
            (0,0,0,0), # 0 (unused)
            (0,0,0,0), # 1
            (1,0,0,0), # 2
            (0,1,0,0), # 3
            (2,0,0,0), # 4
            (0,0,1,0), # 5
            (1,1,0,0), # 6
            (0,0,0,1), # 7
            (3,0,0,0), # 8
            (0,2,0,0)  # 9
        ]
        
        n = len(num)
        
        # Precompute the requirements after factoring in digits sequentially matched with num's prefix
        req_prefix = [(counts[0], counts[1], counts[2], counts[3])]
        first_zero = -1
        
        for i in range(n):
            if num[i] == '0' and first_zero == -1:
                first_zero = i
            d = int(num[i])
            prev = req_prefix[-1]
            df = DIGIT_FACTORS[d]
            req_prefix.append((
                prev[0] - df[0],
                prev[1] - df[1],
                prev[2] - df[2],
                prev[3] - df[3]
            ))
            
        # Step 2: Check if num is inherently perfectly valid
        if first_zero == -1 and get_min_len(req_prefix[-1]) == 0:
            return num
            
        def build(length, req, prefix_str):
            ans = list(prefix_str)
            curr_req = req
            for pos in range(length):
                rem_len = length - 1 - pos
                for d in range(1, 10):
                    df = DIGIT_FACTORS[d]
                    new_req = (
                        curr_req[0] - df[0],
                        curr_req[1] - df[1],
                        curr_req[2] - df[2],
                        curr_req[3] - df[3]
                    )
                    # Pick smallest digit where the remainder sequence can still fulfill the required product
                    if get_min_len(new_req) <= rem_len:
                        ans.append(str(d))
                        curr_req = new_req
                        break
            return "".join(ans)
            
        # Step 3: Check longest matching prefixes to locate the smallest strictly greater integer
        for i in range(n - 1, -1, -1):
            if first_zero != -1 and i > first_zero:
                continue
            
            base_req = req_prefix[i]
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                df = DIGIT_FACTORS[d]
                new_req = (
                    base_req[0] - df[0],
                    base_req[1] - df[1],
                    base_req[2] - df[2],
                    base_req[3] - df[3]
                )
                rem_len = n - 1 - i
                if get_min_len(new_req) <= rem_len:
                    return build(rem_len, new_req, num[:i] + str(d))
                    
        # Step 4: No valid combination is found in `n` length, increment constraint lengths
        min_required_len = get_min_len(req_prefix[0])
        next_len = max(n + 1, min_required_len)
        return build(next_len, req_prefix[0], "")
