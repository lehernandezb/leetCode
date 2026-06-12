class Solution(object):
    
    #Solution to question 15. same idea as two sum but you keep the first index locked and have a two pointer slider.
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            
            while j < k:
                total = nums[i] + nums[k] + nums[j]

                if total == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -=1
        return output
