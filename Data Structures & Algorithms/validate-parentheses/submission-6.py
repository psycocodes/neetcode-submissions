class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            stack.append(char)
            print(f"Before: {stack}")
            if len(stack) >= 2 and stack[-1] == self.reverse(stack[-2]) and stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()
            print(f"After: {stack}")
        return len(stack) == 0

    def reverse(self, bracket):
        return {x[0]: x[1] for x in ["()", "{}", "[]"]}.get(bracket, bracket)

        