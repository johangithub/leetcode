class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_odd = sum([v & 1 for v in collections.Counter(s).values()])
        odd = 1 if num_odd > 0 else 0
        return len(s) - num_odd + oddg