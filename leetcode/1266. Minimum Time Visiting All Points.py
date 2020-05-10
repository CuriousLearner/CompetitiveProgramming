# https://leetcode.com/problems/minimum-time-visiting-all-points/


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        duration = 0
        for point_1, point_2 in zip(points[0:], points[1:]):
            x_dist = abs(point_1[0] - point_2[0])
            y_dist = abs(point_1[1] - point_2[1])
            duration += max(x_dist, y_dist)
        return duration
