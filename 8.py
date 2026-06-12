class Solution(object):
    # Solution to question 8. I hate string questions. So annoying.
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        bank = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        neg = 1
        negSwtich, off = True, False
        result = []
        s = s.strip()
        if s == "": return 0
        for char in s:
            if char == "-" and negSwtich:
                neg = -1
                negSwtich = False
            elif char in bank:
                result.append(char)
                off = True
                negSwtich = False
            elif char == "+":
                continue
            elif char not in bank and off == False:
                return 0
            else:
                break
        if not result: return 0
        total = "".join(result)
        total = int(total) * neg
        if total > 2**31 - 1:
            return 2**31 - 1
        elif total < -2**31:
            return -2**31
        else:
            return total
