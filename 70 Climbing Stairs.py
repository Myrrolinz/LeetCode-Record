class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        prev1, prev2 = 1, 2
        for i in range(3, n+1):
            sum_ = prev1 + prev2
            prev1, prev2 = prev2, sum_

        return prev2