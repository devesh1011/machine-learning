class neighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        n = len(self.grid)
        for i in range(n):
            for j in range(n):
                if self.grid[i][j] == value:
                    adjacent_sum = 0

                    if i > 0:
                        adjacent_sum += self.grid[i - 1][j]
                    if i < n - 1:
                        adjacent_sum += self.grid[i + 1][j]
                    if j > 0:
                        adjacent_sum += self.grid[i][j - 1]
                    if j < n - 1:
                        adjacent_sum += self.grid[i][j + 1]
                    return adjacent_sum

        return 0

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        n = len(self.grid)
        for i in range(n):
            for j in range(n):
                if self.grid[i][j] == value:
                    diagonal_sum = 0

                    if i > 0 and j > 0:
                        diagonal_sum += self.grid[i - 1][j - 1]  
                    if i > 0 and j < n - 1:
                        diagonal_sum += self.grid[i - 1][j + 1]  
                    if i < n - 1 and j > 0:
                        diagonal_sum += self.grid[i + 1][j - 1]  
                    if i < n - 1 and j < n - 1:
                        diagonal_sum += self.grid[i + 1][j + 1]  
                    return diagonal_sum
        return 0


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
