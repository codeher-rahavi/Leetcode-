class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        r = len(matrix)
        c = len(matrix[0])
        arr =[[-1]* r for _ in range(r)]
        for row in range(r):
            for col in range(c):
                if matrix[row][col] == matrix[col][row]:
                    arr[row][col]=1
                elif matrix[row][col] != matrix[col][row] and arr[row][col]==-1:
                    temp  = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row]= temp

                    arr[row][col] =1
                    arr[col][row]=1


        for i in range(r):
            matrix[i] = matrix[i][::-1]

        