def find_duplicate(nums):
    nums.sort()
    if len(nums) < 2:
        return False
    for index in range(len(nums)-1):
        if type(nums[index]) is str or nums[0] < 1:
            return False
        if nums[index] == nums[index+1]:
            return nums[index]
    return False
