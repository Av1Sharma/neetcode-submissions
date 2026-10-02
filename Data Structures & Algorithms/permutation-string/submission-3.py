class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}

        for char in s1:
            target[char] = target.get(char, 0) + 1

        left = 0

        for right in range(len(s2)):
            # add incoming character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # if window is too big, remove outgoing character
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # compare frequencies
            if window == target:
                return True

        return False