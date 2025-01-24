class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}  # Memoization to store whether a node is safe or not

        def dfs(i, visited):
            if i in safe:
                return safe[i]
            if i in visited:
                # If the node is in the current path, it's part of a cycle
                safe[i] = False
                return False
            visited.add(i)
            for nei in graph[i]:
                if not dfs(nei, visited):
                    safe[i] = False
                    return False
            visited.remove(i)
            safe[i] = True
            return True

        res = []
        for i in range(n):
            if dfs(i, set()):  # Pass a new visited set for each DFS call
                res.append(i)
        return res