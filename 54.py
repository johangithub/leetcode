"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5]. 
"""

class Solution:
    def __init__(self):
        print(self.spiralOrder3([[1,2,3],[4,5,6]]))
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==1:
            return matrix[0]
        elif len(matrix)==0:
            return []
        m=matrix
        i,j = 0,0
        d = [0,1]
        ans=[]
        while m[i][j] != 'x':
            if d==[0,1] and (j+1==len(m[0]) or m[i][j+d[1]] == 'x'):
                d = [1,0]
            elif d==[1,0] and (i+1==len(m) or m[i+d[0]][j] == 'x'):
                print(i,j)
                d = [0, -1]
            elif d==[0,-1] and (j==0 or m[i][j+d[1]] == 'x'):
                d = [-1, 0]
            elif d==[-1,0] and (i==0 or m[i+d[0]][j] == 'x'):
                d = [0, 1]
            ans.append(m[i][j])
            m[i][j] = 'x'
            i += d[0]
            j += d[1]
            # print(m, ans)
        return ans

    # @StefanPochmann
    def spiralOrder2(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder2([*zip(*matrix)][::-1])

    # Modified for easier understanding
    def spiralOrder3(self, matrix):
        ans = []
        while len(matrix) > 0:
            ans += matrix[0]
            matrix.pop(0)
            matrix = [*zip(*matrix)][::-1]
        return ans

Solution()
a=[[1,2,3],[4,5,6]]
# print([*zip(*a)])
# print(list(map(list, zip(*a))))
# print([list(x) for x in zip(*a)])
