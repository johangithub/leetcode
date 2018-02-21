"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
import math
class Solution:
    def __init__(self, runs):
        for run in runs:
            print(self.findNthDigit(run['n']))
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        argnumDigits = [(i)*9*(10**(i-1)) for i in range(10)]
        numDigits = 0
        for i in range(len(argnumDigits)):
            if argnumDigits[i] > n:
                numDigits = i
                break

        n -= int(sum(argnumDigits[:numDigits]))

        #now n is nth digit within the digit class
        nthNum = math.ceil(n/numDigits)
        actualNumber = 10 ** (numDigits-1) + (nthNum - 1)
        if n % numDigits == 0:
            return actualNumber % 10
        else:
            target = n % numDigits
            while target < numDigits:
                actualNumber //= 10
                target += 1
            return actualNumber % 10

runs = []
runs.append({"n": 5})
runs.append({"n": 11})
runs.append({"n": 200})
Solution(runs)