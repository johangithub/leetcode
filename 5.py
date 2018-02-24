"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

 

Example:

Input: "cbbd"

Output: "bb"

"""
class Solution:
    def __init__(self, runs):
        for run in runs:
            print(self.longestPalindrome3(run['s']))

    # N^3
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False]*len(s) for x in range(len(s))]

        def isPal(st):
            print(st, st[::-1], st==st[::-1])
            return st==st[::-1]

        max_len = 0
        long_palin = ''
        for cur_len in range(1,len(s)+1):
            for i in range(len(s)-cur_len + 1):
                dp[cur_len-1][i] = isPal(s[i:i+cur_len])
                if dp[cur_len-1][i]:
                    if cur_len > max_len:
                        max_len = cur_len
                        long_palin = s[i:i+cur_len]
                
        return long_palin

    def longestPalindrome2(self, s):
        res = ''
        def palin(s,l,r):
            while l>=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(len(s)):
            res = max(palin(s,i,i), palin(s, i, i+1), res, key=len)
        return res

    def longestPalindrome3(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        def isPalin(sub):
            return sub == sub[::-1]
        print(s)
        for i in range(len(s)):
            print(i)
            if i-maxLen >=1 and isPalin(s[i-maxLen-1:i+1]):
                print('1',s[i-maxLen-1:i+1])
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and isPalin(s[i-maxLen:i+1]):
                print('2',s[i-maxLen:i+1])
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]   
runs = []
runs.append({'s': 'bbbxasdffdsaddddd'})
runs.append({'s': 'banana'})
Solution(runs)
