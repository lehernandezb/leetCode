class Solution(object):
    
    # Solution to question 36
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        dic = {'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = dic[board[i][j]]
                    boxIndex = (i // 3) * 3 + (j // 3)
                    if rows[i][num - 1] or cols[j][num - 1] or boxes[boxIndex][num - 1]:
                        return False
                    rows[i][num - 1] = cols[j][num - 1] = boxes[boxIndex][num - 1] = True
        return True
