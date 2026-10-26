 
class Solution:
    def closedIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            if grid[i][j] == 1:
                return True

            grid[i][j] = 1

            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return up and down and left and right

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count



if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]

    obj = Solution()
    result = obj.closedIsland(grid)

    print("Number of Closed Islands:", result)

    
