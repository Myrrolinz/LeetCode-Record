class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        # cnt = 0
        # i, j = 0, 0

        # while i < len(g) and j < len(s):
        #     print(f"g[i]:{g[i]}; s[j]: {s[j]}")
        #     if g[i] <= s[j]:
        #         cnt += 1
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        # return cnt


        idx = 0
        for i in range(len(s)):
            if idx < len(g) and g[idx] <= s[i]:
                idx += 1
        return idx