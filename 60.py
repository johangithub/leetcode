"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
import math
class Solution:
    def __init__(self, n, k):
        print(self.getPermutation2(n,k))
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = {}
        fact[1] = 1
        def factorial(n):
            if n in fact:
                return fact[n]
            fact[n] = n * factorial(n-1)
            return fact[n]
        factorial(n)
        nums = list(range(1,n+1))
        
        def findDigit(digit, nums, k):
            ind = n - digit - 1
            for i in range(len(nums)):
                if k/fact[ind] <= i + 1:
                    k -= i * fact[ind]
                    return nums[i], k
                    
        res = []
        for digit in range(n-1):
            tmp, k = findDigit(digit, nums, k)
            res.append(tmp)
            nums.remove(res[-1])
        res += nums
        ans = ''.join([str(x) for x in res])
        return ans
        
    # @dasheng2
    def getPermutation2(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            print(numbers, k)
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])
        return permutation

Solution(4,7)