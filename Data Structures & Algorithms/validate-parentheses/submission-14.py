class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in bracket_dict:
                if stack and bracket_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []