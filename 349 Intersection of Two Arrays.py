class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # from collections import defaultdict
        # dict1 = defaultdict(int)
        # for num in nums1:
        #     dict1[num] = dict1.get(num, 0) + 1
        
        # res = set()
        # for num in nums2:
        #     if num in dict1:
        #         res.add(num)
            
        # return list(res)
        from collections import Counter
        cnt1 = Counter(nums1)
        res = set()
        for num in cnt1.keys():
            if num in nums2:
                res.add(num)

        return list(res)
    
    
    # 两种写法
