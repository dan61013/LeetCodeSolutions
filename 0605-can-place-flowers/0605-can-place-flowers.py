class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # init the previous pointer equal 0
        prev_ptr = 0
        # interate
        for i in range(len(flowerbed)):
            # break the loop (n == 0)
            if not n:
                return True
            # set prev & next pointer
            if i:
                prev_ptr = flowerbed[i-1]
            if i != len(flowerbed) - 1:
                next_ptr = flowerbed[i+1]
            else:
                # for the last element
                next_ptr = 0
            # plant new flower when continuously 3 position are available
            if not prev_ptr and not flowerbed[i] and not next_ptr:
                flowerbed[i] = 1
                n -= 1
                continue
        return not n