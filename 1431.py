class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = 0
        output = []
        for i in range(len(candies)):
            if candies[i] > greatest:
                greatest = candies[i]

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                output.append(True)
            else:
                output.append(False)

        return output