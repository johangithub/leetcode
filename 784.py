"""
Given a string S, we can transform every letter individually to be
lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""

class Solution:
    def __init__(self, runs):
        for run in runs:
            print(self.letterCasePermutation(run['S']))
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        cur = []
        for i in range(len(S)):
            if S[i].isalpha():
                if len(cur) == 0:
                    cur.append(S[:i]+S[i].lower()+S[i+1:]) 
                    cur.append(S[:i]+S[i].upper()+S[i+1:])
                else:
                    for word in cur[:]:
                        cur.append(word[:i]+word[i].lower()+word[i+1:]) 
                        cur.append(word[:i]+word[i].upper()+word[i+1:]) 
        if len(cur) == 0:
            return [S]

        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        import itertools
        print([i for i in itertools.product(*L)])

        return list(set(cur))

runs = []
runs.append({'S': "abc"})
runs.append({'S': "a1b2"})
runs.append({'S': "3z4"})
runs.append({'S': "12345"})
Solution(runs)