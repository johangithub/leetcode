from math import sqrt
memo = {}
factor_memo = {}
memo[1] = 0
class Solution:
    def __init__(self):
        nums = [10,20,30]
        print([self.minSteps(num) for num in nums])
    def minSteps(self,num):
        """
        :type n: int
        :rtype: int
        """
        # If prime, return n

        # If not, find the largest factor and divide by the number and add minSteps(largest_factor)

        def factors(n):
            if n in factor_memo:
                return factor_memo[n]
            ans = list(set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup))
            ans.remove(n)
            factor_memo[n] = ans
            return factor_memo[n]

        if num in memo:
            return memo[num]
        else:
            factors = factors(num)
            if len(factors) == 1:
                memo[num] = num
            else:
                memo[num] = min([self.minSteps(f)+num//f for f in factors])

            return memo[num]

Solution()