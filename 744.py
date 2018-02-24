"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
    letters has a length in range [2, 10000].
    letters consists of lowercase letters, and contains at least 2 unique letters.
    target is a lowercase letter.
"""
import bisect
class Solution:
    def __init__(self, runs):
        for run in runs:
            print(self.nextGreatestLetter2(run['letters'], run['target']))
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        lo = 0
        hi = len(letters)-1
        while lo < hi:
            mid = (hi+lo) // 2
            midval = letters[mid]
            print(target, midval, lo, mid, hi)
            if midval <= target:
                lo = mid+1
            elif midval > target:
                hi = mid
            
        return letters[lo]

    # @ManualP
    def nextGreatestLetter2(self, letters, target):
        return letters[bisect.bisect(letters, target) % len(letters)]


runs = []
runs.append({'letters': ['c','f','j','y'], 'target': 'a'})
runs.append({'letters': ['c','f','j','y'], 'target': 'c'})
runs.append({'letters': ['c','f','j','y'], 'target': 'd'})
runs.append({'letters': ['c','f','j','y'], 'target': 'g'})
runs.append({'letters': ['c','f','j','y'], 'target': 'j'})
runs.append({'letters': ['c','f','j','y'], 'target': 'k'})
runs.append({'letters': ['c','f','j','y'], 'target': 'y'})
runs.append({'letters': ['c','f','j','y'], 'target': 'z'})
Solution(runs)