class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        k = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        k = 0
                        continue
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                
        for i in range(1,m):
            if matrix[i][0] == 0: 
                matrix[i] = [0]*n

        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if k == 0:
            matrix[0] = [0]*n


        