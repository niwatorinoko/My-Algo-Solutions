// class Solution {
// public:
//     int longestSubarray(std::vector<int>& nums, int limit) {
//         std::multiset<int> window;
//         int left = 0, maxLength = 0;

//         for (int right = 0; right < nums.size(); ++right) {
//             window.insert(nums[right]);

//             while (*window.rbegin() - *window.begin() > limit) {
//                 window.erase(window.find(nums[left]));
//                 ++left;
//             }

//             maxLength = std::max(maxLength, right - left + 1);
//         }

//         return maxLength;
//     }
// };