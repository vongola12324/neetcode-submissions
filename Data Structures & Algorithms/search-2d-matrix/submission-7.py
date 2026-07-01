class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_left, r_right = 0, len(matrix) - 1
        while r_left < r_right:
            r_mid = (r_left + r_right + 1) // 2   # 上取整，避免死循環
            if matrix[r_mid][0] <= target:
                r_left = r_mid
            else:
                r_right = r_mid - 1
        c_left = 0
        c_right = len(matrix[r_left]) - 1
        while c_left <= c_right:
            c_mid = (c_left+c_right) // 2
            if matrix[r_left][c_mid] == target:
                return True
            elif matrix[r_left][c_mid] > target:
                c_right = c_mid - 1
            else:
                c_left = c_mid + 1
        return False
