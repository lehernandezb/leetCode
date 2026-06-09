# Solution beats 100% of other solutions
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            found = target - nums[i]
            if found in seen:
                return [seen[found], i]
            seen[nums[i]] = i
        return []