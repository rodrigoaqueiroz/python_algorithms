def find_duplicate(nums):
    nums.sort()
    try:
        if len(nums) < 2 or nums[0] < 1:
            return False
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                return nums[index]
        return False
    except (TypeError, ValueError):
        return False
