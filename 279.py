"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. 
"""
from collections import deque

#BFS but too slow
def numSquares(n):
    ans = 0
    q = deque([n,'end'])
    while q:
        node = q.popleft()
        if node == 0:
            return ans
        if node == 'end' and len(q) == 0:
            return -1
        if node == 'end':
            ans += 1
            q.append('end')
        else:
            q.extend([node-x**2 for x in range(1,int(node**0.5)+1)])

    return ans

# Mathematical using Lagrange's Four Square theorem
def numSquares_math(n):
    if int(n**0.5)**2 == n:
        return 1

    while n % 4 ==0:
        n //= 4
    if n % 8 ==7:
        return 4

    for i in range(1, int(n**0.5)+1):
        if int((n-i**2)**0.5)**2 == n-i**2:
            return 2
    return 3

# BFS Accepted
def numSquares_BFS(n):
    if n == 1:
        return 1
    lst = [x**2 for x in range(1,int(n**0.5)+1)]
    toCheck = {n}
    cnt = 0
    while toCheck:
        print(toCheck)
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x<y:
                    break
                temp.add(x-y)

        toCheck = temp
    return cnt

#BFS barely accepted (1652ms)
def numSquares_BFS2(n):
    ans = 1
    q = deque([n,'end'])
    lst = [x**2 for x in range(1,int(n**0.5)+1)]
    while q:
        node = q.popleft()
        if node == 'end' and len(q) == 0:
            return -1
        if node == 'end':
            ans += 1
            q.append('end')
        else:
            for y in lst:
                if node==y:
                    return ans
                if node<y:
                    break
                else:
                    q.extend([node-y])
    return ans
print(numSquares_BFS2(10000))
