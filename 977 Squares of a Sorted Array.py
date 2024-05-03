def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    new_num = [0] * len(nums)
    i = len(nums) - 1
    while(left < right):
        print(f"left: {left}, right: {right}, i: {i}")
        if(abs(nums[right]) > abs(nums[left])):
            new_num[i] = nums[right] ** 2
            i -= 1
            right -= 1
        elif(abs(nums[right]) < abs(nums[left])):
            new_num[i] = nums[left] ** 2
            i -= 1
            left += 1
        else:
            new_num[i] = nums[left] ** 2
            i -= 1
            left += 1
    new_num[0] = nums[left] ** 2
    return new_num
    
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))