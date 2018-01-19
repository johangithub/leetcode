"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
"""

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def dfs(i,j):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and int(grid[i][j]) == 1:
            grid[i][j] = 0
            list(map(dfs, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            return 1
        return 0
    return sum(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))
print(numIslands(grid))