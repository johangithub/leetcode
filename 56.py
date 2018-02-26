# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def __init__(self,runs):
        for intervals in runs:
            print(self.merge(intervals))
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) ==0:
            return []
        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        ans = [intervals.pop(0)]
        while intervals:
            r = intervals.pop(0)

            if ans[-1].end >= r.start and ans[-1].end < r.end:
                ans[-1].end = r.end
            elif ans[-1].end < r.start:
                ans.append(r)
        return ans

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

runs=[]
runs.append([Interval(s=1,e=3),Interval(s=2,e=6),Interval(s=8,e=10),Interval(s=15,e=18)])
runs.append([Interval(s=1,e=4),Interval(s=0,e=0)])
runs.append([Interval(s=1,e=4),Interval(s=0,e=1),Interval(s=0,e=0)])
Solution(runs)