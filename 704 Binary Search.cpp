class Solution {
public:
    // 左闭右开写法
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size();// 注意这里不需要-1
        while (left < right) {// 左闭右开区间
            int mid = left + ((right - left) >> 1); // 注意，这里的右移符号一定要括号起来
            if (nums[mid] < target)
                left = mid + 1; // 由于左闭右开，mid不可能是target，所以一定要mid + 1
            else if (nums[mid] > target)
                right = mid;
            else
                return mid;
        }
        return -1;
    }
};