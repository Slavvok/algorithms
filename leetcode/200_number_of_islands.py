"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        to_visit = [(0, 0)]
        count = 0
        i = 0
        j = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    self._bfs(grid, )
                else:
                    to_visit.pop()
            print(visited)
            if visited:
                count += 1
                visited = []
            if i < len(grid):
                i += 1
            elif j < len(grid[0]):
                j += 1
            to_visit.append((i, j))

        return count


class Solution2:
    def numIslands(self, grid: list[list[str]]) -> int:
        out = 0
        n_rows, n_cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1":
                    out += 1

                    # traverse subgraph aka island
                    stack = deque([(r, c)])  # for O(1) pop first
                    while stack:
                        r0, c0 = stack.pop()
                        if 0 <= r0 < n_rows and 0 <= c0 < n_cols and grid[r0][c0] == "1":
                            grid[r0][c0] = "0"
                            for rd, cd in dirs:
                                stack.append((r0 + rd, c0 + cd))

        return out


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result = Solution().numIslands(grid)
    print(result)
