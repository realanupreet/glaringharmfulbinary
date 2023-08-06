bool subsetsum(vector<int> &nums, int n, int target, vector<vector<int>> &memo) {
    if (target == 0) {
        return true;
    }
    if (n == 0) {
        return false;
    }
    if (memo[n][target] != -1) {
        return memo[n][target];
    }
    if (nums[n - 1] <= target) {
        memo[n][target] = subsetsum(nums, n - 1, target - nums[n - 1], memo) || subsetsum(nums, n - 1, target, memo);
        return memo[n][target];
    } else {
        memo[n][target] = subsetsum(nums, n - 1, target, memo);
        return memo[n][target];
    }
}
class Solution {
public:
    bool canPartition(vector<int> &nums) {
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
        }
        if (sum % 2 != 0) {
            return false;
        }
        vector<vector<int>> memo(nums.size() + 1, vector<int>(sum / 2 + 1, -1));

        return subsetsum(nums, nums.size(), sum / 2, memo);
    }
};