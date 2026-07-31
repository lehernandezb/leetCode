class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0

        if len(flowerbed) <= 1:
            if flowerbed[0] == 0:
                count += 1
            return count >=n
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1

        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            count += 1

        return count >= n