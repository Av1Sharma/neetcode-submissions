class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                   return strs[0][:i]

                
        