class Solution:
    def isPalindrome(self, s: str) -> bool:

        start, end = 0, len(s) - 1


        s = s.strip()
        s = s.lower()
        while start < end:

            if not s[start].isalpha():
                start +=1
            if not s[end].isalpha():
                end -=1

            if s[start] != s[end]:
                return False
            else:
                start +=1
                end -=1

        return True

            


        