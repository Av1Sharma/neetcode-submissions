class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {
            ')' : '(',
            '}' : '{', 
            ']' : '['
        }
        for char in s:
            if char not in dict1.keys():
                stack.append(char)
            elif stack[-1] != dict1[char]:
                return False
            else:
                stack.pop()
        return len(stack) == 0