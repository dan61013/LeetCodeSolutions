class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return self(nums) if nums's length is less than 2
        if len(nums) < 2:
            return nums
        # Set 3 pointer: 0, 1, 2
        red = 0
        white = 0
        blue = len(nums) - 1
        # Stop the while loop if white index better than blue
        while white <= blue:
            # current(white) equal 0, and then go to next index (white & red)
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            # keep
            elif nums[white] == 1:
                white += 1
            else:
                # exchange the white(current) and the last position (blue)
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1