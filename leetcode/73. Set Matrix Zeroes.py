# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # This solution uses O(1) space, as we'll use
        # the first row and first col of the matrix
        # as the markers
        is_first_row_zero = False
        is_first_col_zero = False

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                is_first_row_zero = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_first_col_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if is_first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if is_first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix
