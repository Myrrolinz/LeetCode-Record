class Solution {
public:
    // 双指针法，从头尾分别开始
    vector<int> sortedSquares(vector<int>& nums) {
        int i = 0;
        int j = nums.size() - 1;
        vector<int> new_nums(nums.size(), 0);
        for (int cnt = nums.size() - 1; cnt >= 0; cnt--) {
            if (abs(nums[j]) > abs(nums[i])) {
                new_nums[cnt] = pow(nums[j--], 2);
            } else {
                new_nums[cnt] = pow(nums[i++], 2);
            }   
        }
        return new_nums;
    }
};