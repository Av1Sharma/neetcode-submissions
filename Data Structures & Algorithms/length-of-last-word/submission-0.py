class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        list1 = s.split()

        lt = len(list1)

        return len(list1[lt-1])
        