# 错误答案：比较的时候只想到了左和右谁更小，它没有考虑子数组的总和
# def minSubArrayLen(target: int, nums) -> int:
#     min_len = len(nums)
#     left = 0
#     right = len(nums) - 1
#     the_sum = sum(nums)
#     if(the_sum < target):
#         return 0
#     while(the_sum >= target):
#         if(nums[right] > nums[left]):
#             left += 1
#         elif(nums[right] < nums[left]):
#             right -= 1
#         else:
#             left += 1
#         min_len -= 1
#         the_sum = sum(nums[left: right+1])
#         print(f"left: {left}, right: {right}, min_len: {min_len}, the_sum: {the_sum}")
#     print(nums[left: right+1])
#     return min_len+1


def minSubArrayLen(s: int, nums) -> int:
    l = len(nums)
    left = 0
    right = 0
    min_len = float('inf')
    cur_sum = 0 #当前的累加值
    
    while right < l:
        cur_sum += nums[right]
        
        while cur_sum >= s: # 当前累加值大于目标值
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1
            print(f"left: {left}, right: {right}, min_len: {min_len}, cur_sum: {cur_sum}, nums: {nums[left: right+1]}, min_len: {min_len}")
        
        right += 1
        print(f"right: {right}")
    return min_len if min_len != float('inf') else 0
    
nums = [40, 1, 1, 1, 50, 1]
target = 50
print(minSubArrayLen(target, nums))