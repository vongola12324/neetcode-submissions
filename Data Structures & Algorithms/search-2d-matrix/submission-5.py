class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_left = 0
        r_right = len(matrix) - 1
        while r_left < r_right:
            r_mid = (r_left+r_right) // 2
            print(r_left, r_mid, r_right)

            if matrix[r_mid][0] == target or matrix[r_left][0] == target or matrix[r_right][0] == target:
                return True
            elif matrix[r_mid][0] < target:
                r_left = r_mid + 1
                if matrix[r_left][0] > target:
                    r_left -= 1
                    break
            else:
                r_right = r_mid - 1
        print(r_left, r_right)
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
