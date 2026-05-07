class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in dictionary:
                if len(stack) == 0:
                    return False
                if stack[-1] != dictionary[i]:
                    return False
                del stack[-1]
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        return False