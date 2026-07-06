class Solution(object):

    # Pretty hard one, but I will try and explain it
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        # We are making a ixj matrix where i is the length of the string + 1 (to account for an empty string)
        # and j is the length of the patern + 1 (to account for an empty string), all filled with none
        matrix = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]

        # We are going to make a DFS to recursive solution
        def dfs(i,j):

            # If the matrix slot is already filled retrun true (we are done)
            if matrix[i][j] is not None:
                return matrix[i][j]
            
            # if we are at the end of the j axis of the matrix, return true or not if the string axis is also at the end of the matrix and they are a match or not
            if j == len(p):
                return i == len(s)
            
            # Same here but with a string
            if i == len(s):

                # If the string axsis is not even then return false since there can no longer be a pattern to repeat witg stars
                if (len(p) - j) % 2 == 1:
                    return False
                
                # Search through the pattern string and if there is only stars left then it will be true
                for k in range(j + 1, len(p), 2):
                    if p[k] != '*':
                        return False
                return True
            
            # Match is true or false if the chars are the same or if there is a period
            match = s[i] == p[j] or p[j] == "."

            # Check if the next following char is a star to see if they can cover the current string
            if j < len(p) - 1 and p[j + 1] == "*":
                result = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else: 
                result = match and dfs(i + 1, j +  1)
            matrix[i][j] = result
            return result
        
        return dfs(0,0)