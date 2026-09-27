class Solution:
    def calPoints(self, operations: List[str]) -> int:
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        stack = []

        for i in range(len(operations)):
            if is_number(operations[i]):
                stack.append(int(operations[i]))
            if operations[i] == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            if operations[i] == "D":
                stack.append(int(stack[-1]) * 2)
            if operations[i] == "C":
                stack.pop()
        total = 0
        for num in stack:
            total += num

        return total