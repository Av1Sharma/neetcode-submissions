class Solution:
    def maxDifference(self, s: str) -> int:
        ## sorry im still tripping
        hash1 = {}


        for char in s:
            result = hash1.get(char, 0) + 1

            hash1[char] = result

        maxOdd = 0
        minEven = 100000000
        for key, val in hash1.items():
            if val % 2 == 0:
                minEven = min(minEven, val)
            else:
                maxOdd = max(maxOdd, val)
        
        return maxOdd - minEven

        