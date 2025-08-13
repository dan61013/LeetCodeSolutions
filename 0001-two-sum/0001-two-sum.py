class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hash_table:
                return [hash_table[diff], i]
            else:
                hash_table[nums[i]] = i

