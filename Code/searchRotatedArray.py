class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] < target:
                if nums[start] <= target and nums[start] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] > target:
                if nums[end] >= target and nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
