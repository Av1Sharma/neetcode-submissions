class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        arr = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
               if i != j:
                arr[j][i] = matrix[i][j]
               else:
                arr[j][i] = matrix[i][j]
        return arr
        