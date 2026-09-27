class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            nleft = numbers[left]
            nright = numbers[right]
            if nleft+ nright > target:
                right -=1
            if nleft + nright < target:
                left +=1
            if nleft + nright == target:
                return [left+1, right+1]
            