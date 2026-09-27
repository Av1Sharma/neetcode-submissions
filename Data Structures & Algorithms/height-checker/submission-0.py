class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        h = sorted(heights)

        count = 0
        for i in range(len(h)):
            if heights[i] != h[i]:
                count +=1

        return count