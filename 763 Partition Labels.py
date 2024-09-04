class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {}
        for i, j in enumerate(s):
            last_occur[j] = i

        start = 0
        end = 0
        result = []
        for i in range(len(s)):
            if last_occur[s[i]] > end:
                end = last_occur[s[i]]
            if i == end:
                result.append(end-start+1)
                start = i+1

        return result
