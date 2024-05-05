class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from collections import defaultdict
        tmp = defaultdict(lambda : 0)
        cnt = 0
        for i in nums1:
            for j in nums2:
                tmp[i+j] += 1
        for i in nums3:
            for j in nums4:
                cnt += tmp.get(-(i+j), 0)

        return cnt