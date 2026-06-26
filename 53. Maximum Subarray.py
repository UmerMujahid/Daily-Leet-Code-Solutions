class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_value = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum > max_value:
                max_value = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_value
