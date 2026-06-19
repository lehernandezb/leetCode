class Solution(object):

    # First time doing a recursive method to slove a question. I feel like this was the only way that made sense in my head lol
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits: return []

        key = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []

        def recursiveCombinations(combo, nextDigit):
            if not nextDigit:
                result.append(combo)
                return
            
            for letter in key[nextDigit[0]]:
                recursiveCombinations(combo + letter, nextDigit[1:])
        
        recursiveCombinations("", digits)

        return result