"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        ans=[]
        cnt=0
        for s in strs:
            b=''.join(sorted(s))
            if b in d:
                #find index in ans
                ans[d[b]].append(s)
            else:
                ans.append([s])
                d[b] = cnt
                cnt+=1
        return ans
            
