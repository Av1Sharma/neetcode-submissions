class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ## one more while im tripping. i don't understand this fuck.
        ## basically appending a 0 to each end.
        ## ohhhhh. this way it doesn't go out of bounds

        ## is there no way to do it logically?


        ## ah fuck you. this stupid ass problem.

        flowerbed = [0] + flowerbed + [0]


        for i in range(1, len(flowerbed)-1):

            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                n -=1
                flowerbed[i] = 1

        return n <= 0
        