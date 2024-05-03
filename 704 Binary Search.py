def search(nums, target) -> int:
    mid = len(nums) // 2
    left = 0
    right = len(nums)
    print(f"mid: {mid}, left: {left}, right: {right}")
    while(left < right):
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
            mid = mid // 2
            print(f"mid: {mid}, left: {left}, right: {right}")
        elif nums[mid] < target:
            left = mid + 1
            mid = mid + (right - mid) // 2
            print(f"mid: {mid}, left: {left}, right: {right}")
    return -1

nums = [2,5]
print(search(nums, 2))

# 这题主要的问题在于left = mid + 1，使用的是左闭右开的区间
# 而且不要用递归，直接在函数内进行while循环