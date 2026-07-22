class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
     
        max_value = max(nums)
        min_value = min(nums)
        return (max_value - min_value) * k