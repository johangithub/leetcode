"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""

"""
Let's define index of the once-occuring number to be ind
if a number is in n and n+1 where n % 2 ==0, then ind > n+1
if the same numbers occur at n and n + 1 where n % 2 == 1, then ind < n
"""


#solution credits to @Penghuan
def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start = 0
    end = len(nums) - 1
    while start < end:
        i = (start + end) // 2
        if i % 2 == 1:
            i -= 1

        if nums[i] != nums[i+1]:
            end = i
        else:
            start = i + 2
    return nums[start]
nums = [1,1,2,3,3,4,4,8,8]
nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))