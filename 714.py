"""
Your are given an array of integers prices, for which the i-th element is the price
of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like,
but you need to pay the transaction fee
for each transaction. You may not buy more than
1 share of a stock at a time (ie. you must sell the stock share before you buy again)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""

class Solution:
    def __init__(self, runs):
        for run in runs:
            print(self.maxProfit(run['prices'], run['fee']))
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # (bought, sold, profit)
        dp = [(0,0,0)]*len(prices)
        if len(prices) >= 2:
            if prices[1]>prices[0]+fee:
                dp[1] = (0,1,prices[1]-prices[0]-fee)

        if len(prices)<=2:
            return dp[-1]

        for i in range(2,len(prices)):
            #determine wheter to
            # 1. buy earlier than current profit,
            # 2. buy later than current profit.
            # 3. keep current profit
            p1 = prices[i]-min(prices[:i])-fee
            p2 = dp[i-1][2]+prices[i]-min(prices[dp[i-1][1]:i])-fee
            if p1>p2:
                dp[i] = (prices.index(min(prices[:i])), i, p1)
            else:
                print(i)
                if prices[i] > min(prices[dp[i-1][1]:i]) + fee:
                    dp[i] = (prices.index(min(prices[dp[i-1][1]:i])), i, p2)
                else:
                    dp[i] = dp[i-1]

            print("i: {}, prices: {}, p1: {},p2: {}".format(i,prices[i], p1, p2))
        print(dp)
        return dp[-1][2]

runs = []
# runs.append({'prices': [1,5,3,10], 'fee': 2})
runs.append({'prices': [1,3,2,8,4,9], 'fee': 2})
Solution(runs)