class Solution(object):
    
    # Solution to question 4
    def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            i, j = 0, 0
            merged = []

            while i < len(nums1) and j < len(nums2):
                    if nums1[i] <= nums2[j]:
                            merged.append(nums1[i])
                            i += 1
                    else:
                            merged.append(nums2[j])
                            j += 1
            
            merged.extend(nums1[i:])
            merged.extend(nums2[j:])

            n = len(merged)

            if n % 2 != 0:
                    return merged[((n) // 2)]
            else:
                    a = merged[n//2 - 1]
                    b = merged[n//2]
                    return (a + b) / 2.0