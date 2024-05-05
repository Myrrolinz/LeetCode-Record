class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # collections巨快巨爽
        # return collections.Counter(s) == collections.Counter(t)
        from collections import defaultdict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict