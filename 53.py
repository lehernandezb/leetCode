class Solution(object):

    # O(n) solution to question 53. The main idea is to make a choice if we should continue the sub string or start a new one.
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = nums[0]
        currentSum = nums[0]

        for index in range(1, len(nums)):
            if currentSum + nums[index] > nums[index]:
                currentSum += nums[index] 
            else:
                currentSum = nums[index]
            if currentSum > maxSum: maxSum = currentSum 

        return maxSum