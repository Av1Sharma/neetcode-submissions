class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        letterToWord = {}
        wordToLetter = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]

            if letter in letterToWord:
                if letterToWord[letter] != word:
                    return False
            else:
                letterToWord[letter] = word

            if word in wordToLetter:
                if wordToLetter[word] != letter:
                    return False
            else:
                wordToLetter[word] = letter

        return True