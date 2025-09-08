class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev_ptr = 0
        for i in range(len(flowerbed)):
            if not n:
                return True
            # Set prev & next pointer
            if i:
                prev_ptr = flowerbed[i-1]
            if i != len(flowerbed) - 1:
                next_ptr = flowerbed[i+1]
            else:
                next_ptr = 0
            if not prev_ptr and not flowerbed[i] and not next_ptr:
                flowerbed[i] = 1
                n -= 1
                continue
        return not n