class Solution:
    def __init__(self, runs):
        for run in runs:
            print(self.simplifyPath(run))
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        import re
        path = re.sub('/\./','/', path)
        
        path = re.sub('//', '/', path)
        path = re.sub('/$', '', path)
        return path
        

runs =[]
runs.append('/home/')
runs.append('//')
runs.append("/a/./b/../c/")
Solution(runs)