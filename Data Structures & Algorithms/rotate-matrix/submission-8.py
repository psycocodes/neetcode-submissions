class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                print(f"<hswap>:{(i,j)} <-> {(i, n-1-j)}")
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j] 

        for i in range(n):
            for j in range(n-i-1):
                print(f"<dswap>:{(i,j)} <-> {(i, n-1-j)}")
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]