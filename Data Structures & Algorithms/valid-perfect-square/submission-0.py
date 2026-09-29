class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ## this song is fire

        left = 1
        right = num
        while left != right:
            mid = left + right // 2
            if mid ** 2 > num:
                right = mid - 1
            if mid ** 2 < num:
                left = mid + 1
            if mid ** 2 == num:
                return True
        if left * right == num:
            return True
        else:
            return False
        