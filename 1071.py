class Solution(object):
    def gcdOfStrings(self, str1, str2):
            """
            :type str1: str
            :type str2: str
            :rtype: str
            """
            if str1 + str2 != str2 + str1:
                return ""
            
            min_length = min(len(str1), len(str2))
            for size in range(min_length,0,-1):
                if len(str1) % size != 0 or len(str2) % size != 0:
                    continue

                candidate = str1[:size]

                if candidate * (len(str1) // size) == str1 and candidate * (len(str2) // size) == str2:
                    return candidate 
            return ""

