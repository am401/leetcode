class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        result = [[1],[1,1]]
        for i in range(2, n):
            row_list = [1]
            for j in range(1, i):
                row_list.append(result[i - 1][j - 1] + result[i - 1][j])
            row_list.append(1)
            result.append(row_list)
        return result
