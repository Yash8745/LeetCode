from collections import defaultdict
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize adjacency matrix to represent prerequisites
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Populate direct prerequisites
        for prereq, crs in prerequisites:
            is_prerequisite[prereq][crs] = True
        
        # Floyd-Warshall algorithm to find transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True
        
        # Answer queries based on the computed transitive closure
        result = []
        for u, v in queries:
            result.append(is_prerequisite[u][v])
        
        return result
