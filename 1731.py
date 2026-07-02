class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        hightest, curr = 0, 0

        for i in range(len(gain)):
            curr += gain[i]
            if hightest <= curr:
                hightest = curr

        return hightest