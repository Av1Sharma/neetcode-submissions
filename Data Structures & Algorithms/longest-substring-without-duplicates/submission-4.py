class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        left = 0

        for right in range(len(s)):

            while s[right] in s[left:right]:
                left += 1

            best = max(best, right - left + 1)

        return best