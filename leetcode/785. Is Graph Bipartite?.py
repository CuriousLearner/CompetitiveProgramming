# https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = {}
        for from_node in range(len(graph)):
            if from_node in colored:
                continue
            stack = [from_node]
            colored[from_node] = 0
            while stack:
                from_node = stack.pop()
                for to_node in graph[from_node]:
                    if to_node in colored:
                        if colored[to_node] == colored[from_node]:
                            return False
                    else:
                        colored[to_node] = 1 - colored[from_node]
                        stack.append(to_node)
        return True
