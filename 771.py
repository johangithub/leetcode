"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.


"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([1 for x in S if x in J])


def b_search(l, target):
    lo = 0
    hi = len(l) -1
    while lo < hi:
        mid = (hi+lo)//2
        if l[mid]<target:
            lo = mid+1
        else:
            hi = mid
    return lo,l[lo]

print(b_search([4,8,9,10,24,32,45,56],32))

def editDistance(s1,s2):
    if len(s1)==0:
        return len(s2)
    if len(s2) ==0:
        return len(s1)

    #dp[i][j] represents the minimum edit distance of string upto s1[:i] and s2[:j]
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)] 
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i==0:
                dp[i][j] = j
            if j==0:
                dp[i][j] = i           
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

    return dp[-1][-1]

print(editDistance("hello", "hallo"))
