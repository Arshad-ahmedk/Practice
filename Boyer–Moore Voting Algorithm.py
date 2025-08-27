nums=[2,2,1,4,3]
candidate=0
count=0
for num in nums:
    if count == 0:
        candidate = num
    count+=(1 if candidate == num else -1)
print(candidate)


# from collections import Counter
#
# nums = [2, 2, 1, 4, 3]
# freq = Counter(nums)
# most_common_num = max(freq, key=freq.get)
# count = freq[most_common_num]
# print(most_common_num)