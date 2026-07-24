class Solution(object):
    def searchRange(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            def find_bound(is_first):
                low = 0
                high = len(nums) - 1
                bound = -1
                while low <= high:
                    mid = (low + high) // 2
                    if nums[mid] == target:
                        bound = mid
                        if is_first:
                            high = mid - 1
                        else:
                            low = mid + 1

                    elif nums[mid] < target:
                        low = mid + 1
                    else: 
                        high = mid - 1
                
                return bound
            start = find_bound(is_first=True)
            if start == -1:
                return [-1, -1]
            end = find_bound(is_first=False)
            return [start, end]