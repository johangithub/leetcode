# @caikehe
class Solution:
    def __init__(self, nums):
        print(self.subsets1(nums))
        print(self.subsets2(nums))
        print(self.subsets3(nums))

    #dfs
    def subsets1(self, nums):
        self.res = []
        self.dfs(nums, 0, [])
        return self.res
        
    def dfs(self, nums, index, path):
        self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]])

    #iterative
    def subsets2(self, nums):
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res

    #bit manipulation
    def subsets3(self, nums):
        res = []
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
Solution([1,2,3])

a=[1,2,3,5]
a.remove(5)
print(a)