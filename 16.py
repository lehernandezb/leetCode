class Solution(object):
    # Solution to question 16, pretty simple 3sum problem
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        output = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                dif = nums[i] + nums[j] + nums[k]
                
                if dif == target:
                    return dif
                elif dif < target:
                    j += 1
                    if abs(target - dif) <= abs(target - output):
                        output = dif
                else:
                    k -= 1
                    if abs(target - dif) <= abs(target - output):
                        output = dif
    
        return output
