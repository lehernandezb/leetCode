class Solution(object):
    # Solution to question 29, this is so buns
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # Check if it should be positive or negitive
        positive = (dividend < 0) is (divisor < 0)

        # Get numbers in absolute values
        a, b, res = abs(dividend), abs(divisor), 0

        # While the dividend is bigger then the diviser
        while a >= b:
            
            # We have a temp var where we keep on skipping each time we subtract
            # So it looks like 3, 6, 12, 24 to save time
            # We check if it is possible then we add it to the result count.
            temp, i = b, 1
            while a >= (temp << 1):
                  i <<= 1
                  temp <<= 1
            a -= temp
            res += i
                  

        # Edge cases for if it is out of range
        if not positive:
              res = -res
        if res > 2**31 - 1: 
              return 2**31 -1
        elif res < -2**31:
              return -2**31
        return res