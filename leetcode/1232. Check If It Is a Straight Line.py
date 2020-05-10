# https://leetcode.com/problems/check-if-it-is-a-straight-line/


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        first, second = coordinates[0], coordinates[1]
        x1, y1 = first
        x2, y2 = second
        for coord in coordinates[2:]:
            x, y = coord
            if (y1 - y2) * (x - x1) != (y - y1) * (x1 - x2):
                return False
        return True
