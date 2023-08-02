class Solution {
public:
    // slow/fast pointer
    int removeElement(vector<int>& nums, int val) {
        int slow = 0; int fast = 0;
        for (; fast < nums.size(); fast++) {
            if (nums[fast] != val) {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
};