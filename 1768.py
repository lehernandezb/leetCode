class Solution(object):
    def mergeAlternately(self, word1, word2):
            """
            :type word1: str
            :type word2: str
            :rtype: str
            """
            i, j = 0, 0
            isWord1 = True
            output = ""

            while i < len(word1) or j < len(word2):
                if isWord1:
                    if not i < len(word1):
                        output += word2[j::]
                        break
                    output += word1[i]
                    i += 1
                    isWord1 = False
                else:
                    if not j < len(word2):
                        output += word1[i::]
                        break
                    output += word2[j]
                    j += 1
                    isWord1 = True
        
            return output