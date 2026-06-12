class Solution(object):

    # Solution to question 7
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 1 
        if (x < 0): 
            neg = -1
            x = x * neg
        numList = list(str(x))
        multi = 10**(len(numList) - 1)
        num = 0
      
        for i in range(len(numList) - 1, -1, -1):
            num += (multi * int(numList[i]))
            multi = multi // 10
        num = num * neg
        
        return num if (-2**31 < num) and (2**31 > num) else 0;