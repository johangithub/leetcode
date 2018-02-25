"""
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permut(l):
            return [[l[i]]+p for i in range(len(l)) for p in permut(l[:i]+l[i+1:])] or [[]]
        ans = set([tuple(l) for l in permut(nums)])
        return [list(x) for x in ans]          

print(0==False)
