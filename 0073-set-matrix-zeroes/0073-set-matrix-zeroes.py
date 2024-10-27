class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top_left = False

        rows = len(matrix)
        column = len(matrix[0])

        for r in range(rows):
            for c in range(column):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        top_left = True
        

        for r in range(1,rows):
            for c in range(1,column):
                if matrix[r][0] == 0  or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                for c in range(column):
                    matrix[r][0] = 0

        if top_left:
            for r in range(rows):
                for c in range(column):
                    matrix[0][c] = 0

        