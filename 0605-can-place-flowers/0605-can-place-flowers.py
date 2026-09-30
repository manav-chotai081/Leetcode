class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0 and (n == 1 or n == 0):
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 0 and n > 1:
            return False 
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            elif i < len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            else:
                if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
                    flowerbed[len(flowerbed)-1] = 1
                    n -= 1
            if n <= 0:
                return True
        return False