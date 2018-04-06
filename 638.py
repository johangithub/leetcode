def shoppingOffers(price, special, needs):
        d = {}
        def dfs(cur):
            val = sum(cur[i]*price[i] for i in range(len(needs))) #cost without special
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0: # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[-1]) # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val
        return dfs(needs)

runs = []
runs.append({"price": [2,5], "special": [[3,0,5], [1,2,10]], "needs": [3,2]})
for run in runs:
    print(shoppingOffers(**run))


target = 8
nums = [10,1,2,7,6,1,5]

ans =[]
nums.sort()
def dfs(cur, nums,target,path):
    print(nums, target, path)
    if target == 0:
        ans.append(path)
        return
    if target < 0:
        return
    for i in range(cur, len(nums)):
        if i > cur and nums[i]==nums[i-1]:
            continue
        path.append(nums[i])
        
    if nums:
        path.append(nums[0])
        # dfs(nums[1:],target-nums[0],path)
# dfs(0, nums,target, [])
print(ans)
a=[1,2,3,4,5,5,5,5]
from collections import Counter

print(list(Counter(a)))

print(max(a, key=a.count))