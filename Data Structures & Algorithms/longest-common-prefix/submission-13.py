class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            letter = strs[0][i]
            res = strs[0][0:i]
            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return res
        return strs[0]
