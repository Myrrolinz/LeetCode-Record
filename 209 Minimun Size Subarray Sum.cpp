class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int cnt = INT_MAX;
        int i = 0;
        int sum = 0;
        for(int j = 0; j < nums.size(); j++) {
            sum += nums[j];
            // 以下部分为写错的
            // if (sum >= target) {
            //     cnt = min(cnt, j - i + 1);
            //     sum -= nums[i];
            //     i++;
            //     j--;
            //     isReal = true;
            // }
            // if (cnt == 1)
            //     break;
            while (sum >= target) { // ATTEN!!这里需要用while
                cnt = min(cnt, j - i + 1);
                sum -= nums[i++];
            }
        }
        return cnt == INT_MAX ? 0 : cnt;
    }
};