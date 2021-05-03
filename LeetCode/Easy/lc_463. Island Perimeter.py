class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def present(x, y):
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0:
                    count += 1
            return count

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += present(i, j)
        return total