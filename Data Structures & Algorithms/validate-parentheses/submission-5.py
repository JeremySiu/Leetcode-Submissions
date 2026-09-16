class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or (len(s) % 2 != 0):
            return False
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) > 0:
                    bracket = stack.pop()
                    if ((i == ')' and bracket != '(') or 
                        (i == ']' and bracket != '[') or 
                        (i == '}' and bracket != '{')):
                        return False
                else:
                    return False
        return len(stack) == 0