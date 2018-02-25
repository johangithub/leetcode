"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        g=obstacleGrid
        m,n = len(g), len(g[0])
        dp = [[0 for x in range(n)] for x in range(m)]
        dp[0][0] = 1
        i = 0
        while i < m:
            j = 0
            while j < n:
                if g[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if j>0:
                        dp[i][j] += dp[i][j-1]
                    if i>0:
                        dp[i][j] += dp[i-1][j]
                j+=1
            i+=1
        return dp[-1][-1]
        
print(False ^ True ^ False)