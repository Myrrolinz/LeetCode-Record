class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            zeroNum = s.count('0')
            oneNum = len(s) - zeroNum
            for i in range(m, zeroNum - 1, -1):
                for j in range(n, oneNum - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)
        return dp[m][n]