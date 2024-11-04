'''
https://neetcode.io/problems/search-2d-matrix

Used binary search. Treated a 2-D matrix like a 1-D matrix by using a helper get_rc function.
'''

class Solution:

    def get_rc(self, mat, x):
        m,n = len(mat), len(mat[0])
        row = x // n 
        col = x % n
        return row, col

    def search_matrix(self, mat, l, r, target):
        if l > r:
            return False
        
        mid = (l+r)//2

        row, col = self.get_rc(mat, mid)

        if target == mat[row][col]:
            return True
        
        elif target < mat[row][col]:
            return self.search_matrix(mat, l, mid-1, target)
        
        else:
            return self.search_matrix(mat, mid+1, r, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search_matrix(matrix, 0, (len(matrix)*len(matrix[0]))-1, target)