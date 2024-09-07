class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1): # 这是排列问题
            for j in range(i):
                if dp[j] and s[j: i] in sordSet:
                    dp[i] = True
                    break
        return dp[n]
