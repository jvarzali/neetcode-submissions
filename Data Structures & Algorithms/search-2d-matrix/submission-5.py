class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, t, b, row =  0, len(matrix[0]) - 1, 0, len(matrix) - 1, -1

        while t <= b:
            mid = math.floor((t + b) / 2)

            if matrix[mid][l] > target:
                b = mid - 1
            elif matrix[mid][r] < target:
                t = mid + 1
            else:
                t = b + 1
                row = mid
        
        print(row)

        if row == -1:
            return False
        
        while l <= r:
            print(str(l) + " " + str(r))
            mid = math.floor((l + r) / 2)
            print(mid)

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
            print(str(l) + " " + str(r))
            print()
        
        return False