# Given an array of integers, return indices of the two numbers such that they add 
# up to a specific target.

# You may assume that each input would have exactly one solution, and you may not 
# use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

#####################################################################

# naive solution
# go over the list, add number one by one to see if the sum equals to the target
# need to have nested loop
# since we have nested loop, runtime will be O(n^2), not ideal solution

def two_sums(nums, target):

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                return [i, j]


# faster solution
# have a dictionary with num as key and indices as value
# go over dictionary, if target - num is in the dictionary
# we will return their value
# by using hashmap, we reduce our runtime to O(n)

def two_sums(nums, target):

    two_sums_dict = {}

    for i in range(len(nums)):
        two_sums_dict[nums[i]] = i 

    for k, v in two_sums_dict.items():
        complement = target - k
        if complement in two_sums_dict.keys():
            return [v, two_sums_dict[complement]]



print(two_sums([2, 7, 11, 15], 18))



