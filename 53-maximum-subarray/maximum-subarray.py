class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        maxSum = nums[0]

        for i in nums:
            if current_sum < 0:
                current_sum =0
            current_sum += i

            maxSum = max(current_sum , maxSum)

        return maxSum
        