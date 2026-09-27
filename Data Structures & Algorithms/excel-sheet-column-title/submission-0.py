class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        firstLetter = 96 + (columnNumber // 26)
        secondLetter = 96 + (columnNumber % 26)
        str1 = ''
        if firstLetter <= 0:
            str1 += chr(secondLetter)
        else:
            str1 += chr(firstLetter)
            str1 += chr(secondLetter)

        return str1.upper()