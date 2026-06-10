class Solution(object):

    # Solution to question 13, took around 6 minutes
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        bank = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if len(s) == 1:
            return bank[s]
        
        for index, char in enumerate(s[:-1]):
            if char == s[index + 1]:
                total += bank[char]
            elif bank[char] > bank[s[index + 1]]:
                total += bank[char]
            else:
                total -= bank[char]
        total += bank[s[-1]]

        return total