class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while right > left:
                the_sum = nums[i] + nums[left] + nums[right]
                if the_sum > 0:
                    right -= 1
                elif the_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    # 注意下面这个+-的位置，是在else里！！
                    right -= 1
                    left += 1

        return result