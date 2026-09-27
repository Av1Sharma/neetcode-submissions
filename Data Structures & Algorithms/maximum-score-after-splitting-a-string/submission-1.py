class Solution:
    def maxScore(self, s: str) -> int:

        ## i lowkey forgot to hit record, been here for like 5 minutes


        max1 = 0
        for i in range(len(s)-1):

            left = s[:i+1]
            right = s[i+1:]

            cL = left.count('0')
            cR = right.count('1')

            count = cL + cR


            max1 = max(max1, count)

        return max1