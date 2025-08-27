# nums = [1,2,3,4,5,6,7]
# k = 3
# a=[]
# for i in range(len(nums)-1, k, -1):
#     a.append(nums[i])
# for i in range(0, len(nums)-k):
#     a.append(nums[i])
# print(a)

nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
k = k % n
nums[:] = nums[-k:] + nums[:-k]
print(nums)