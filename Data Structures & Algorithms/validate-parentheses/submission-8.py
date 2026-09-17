class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')': '(', '}': '{', ']': '['}
        stack = ['']

        for i in s:
            if i not in bracket_dict:
                stack.append(i)
            elif bracket_dict[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == ['']