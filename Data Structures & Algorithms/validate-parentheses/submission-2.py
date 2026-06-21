class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                if p == ")":
                    if stack.pop() != "(":
                        return False
                elif p == "}":
                    if stack.pop() != "{":
                        return False
                elif p == "]":
                    if stack.pop() != "[":
                        return False
        return len(stack) == 0