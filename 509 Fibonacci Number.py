class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev1, prev2 = 0, 1
        for i in range(2, n+1):
            sum_ = prev1 + prev2
            prev1, prev2 = prev2, sum_

        return prev2