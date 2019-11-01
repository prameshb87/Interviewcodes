"""
Given a list of nums find the subarray of min length such that the elements
add up to at least a number s.
For eg if nums = [2,3,1,2,4,3] and s is 7 then answer is 2 because [4,3] add up to 7
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1 or sum(nums) < s:
            return 0
        # min_len = len(nums)
        # if sum(nums) >= s:
        #     min_len_left = self.minSubArrayLen(s, nums[:len(nums) - 1])
        #     min_len_right = self.minSubArrayLen(s, nums[1:len(nums)])
        #     if min_len_left > 0 and min_len_right > 0:
        #         min_len = min(min_len, min_len_left, min_len_right)
        #     if min_len_left == 0 and min_len_right > 0:
        #         min_len = min(min_len, min_len_right)
        #     if min_len_right == 0 and min_len_left > 0:
        #         min_len = min(min_len, min_len_left)
        # return min_len

        min_len, j, sum = 2**64, 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_len = min(min_length, i + 1 - j)
                sum -= nums[j]
                j += 1
        return min_len if min_len != 2**64 else 0
