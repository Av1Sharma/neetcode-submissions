class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        ## one more while im tripping. i don't understand this fuck.
        ## basically appending a 0 to each end.
        ## ohhhhh. this way it doesn't go out of bounds

        ## is there no way to do it logically?

        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -=1
                    flowerbed[i] = 1
                    break

            if i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    n -=1
                    flowerbed[i] = 1
                    break

            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                n -=1
                flowerbed[i] = 1

        return n <= 0
        