class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        freq = defaultdict(lambda: 0)
        for num in nums:
            freq[num] += 1

        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    last = target - nums[i] - nums[j] - nums[k]
                    if last in freq:
                        cnt = (nums[i] == last) + (nums[j] == last) + (nums[k] == last)
                        if freq[last] > cnt:
                            # 注意下面一定要转换tuple，因为set()中的类型必须immutable
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], last])))

        return [list(x) for x in res]
    
    # 这里其实应该用双指针法来做，就和3sum一样，但是用dict和set逻辑更清晰啊（