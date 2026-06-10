class Solution(object):

    # Question 13, quite easy but there was a way simpler way lmfao
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        value = str(x)

        for index in range(len(value)):
            headptr = index
            tailptr =  (index + 1) * -1
            if headptr == (len(value) - 1):
                return True
            if value[headptr] != value[tailptr]:
                return False
        return True
    
    # Simple ahh way would be this. Python is so sily!
    def simpleIsPalindrome(self, x):
        return str(x) == str(x)[::-1]
    