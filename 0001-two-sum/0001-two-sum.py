class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            subtract = target - nums[i]
            if subtract not in hash_table:
                hash_table[subtract] = i
        return []