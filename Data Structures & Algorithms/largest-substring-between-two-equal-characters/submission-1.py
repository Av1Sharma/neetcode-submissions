class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLen = -1
        for i in range(len(s)):
            if s.count(s[i]) > 1:
                end = s.rfind(s[i], i+1)
                print(end)
                maxLen = max(end-i-1, maxLen)

        return maxLen
        