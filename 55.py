"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false. 
"""

class Solution:
    def __init__(self, nums):
        for nums in runs:
            print(self.canJump(nums))

    # @StefanPochmann
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mx = 0
        for i, n in enumerate(nums):
            if i > mx:
                return False
            mx = max(i+n, mx)
        return True
    
runs = []
runs.append([2,3,1,1,4]) # T
runs.append([0]) # T
runs.append([3,2,1,0,4]) # F
runs.append([0,2,3]) # F
Solution(runs)