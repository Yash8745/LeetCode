class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diag_sq = 0
        best_area = 0

        for length, width in dimensions:
            diag_sq = length**2 + width**2
            area = length * width

            if diag_sq > best_diag_sq or (diag_sq == best_diag_sq and area > best_area):
                best_diag_sq = diag_sq
                best_area = area

        return best_area

            