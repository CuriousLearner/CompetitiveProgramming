# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return
        row_begin, row_end, col_begin, col_end = (
            0,
            len(matrix) - 1,
            0,
            len(matrix[0]) - 1,
        )

        while row_begin <= row_end and col_begin <= col_end:
            for c in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][c])
            row_begin += 1
            for r in range(row_begin, row_end + 1):
                result.append(matrix[r][col_end])
            col_end -= 1
            if row_begin > row_end:
                break
            for c in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][c])
            row_end -= 1
            if col_begin > col_end:
                break
            for r in range(row_end, row_begin - 1, -1):
                result.append(matrix[r][col_begin])
            col_begin += 1

        return result
