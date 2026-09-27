class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {
            ')' : '(',
            '}' : '{', 
            ']' : '['
        }
        if len(s) < 2:
            return False
        for char in s:
            if char not in dict1.keys():
                stack.append(char)
            elif stack[-1] == dict1[char]:
                stack.pop()
            else:
                return False
        return len(stack) == 0