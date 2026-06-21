class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose = { "(": ")", "{": "}", "[": "]" }

        for t in s:
            if t in openToClose:
                stack.append(t)
            else:
                if not stack or openToClose[stack.pop()] != t:
                    return False
        return not stack