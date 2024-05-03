def removeElement(nums, val: int) -> int:
    cnt = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            print(f"i: {i}, nums[i]: {nums[i]}")
            nums[i] = 51
            cnt += 1
    
    print(nums)
    nums.sort()
    print(nums)
    print(len(nums)-cnt)
    nums = nums[: len(nums)-cnt]
    print(nums)
    return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)
# 这题比较牛逼的解法是快满指针法
# def removeElement(self, nums: List[int], val: int) -> int:
#     # 快慢指针
#     fast = 0  # 快指针
#     slow = 0  # 慢指针
#     size = len(nums)
#     while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
#         # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
#         if nums[fast] != val:
#             nums[slow] = nums[fast]
#             slow += 1
#         fast += 1
#     return slow