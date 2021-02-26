class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(','{','[']
        closed_brackets = [')','}',']']
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif i in closed_brackets and not stack:
                return False
            elif i in closed_brackets:
                top = stack[-1]
                if i == ')' and top == '(':
                    stack = stack[0:-1]
                elif i == '}' and top == '{':
                    stack = stack[0:-1]
                elif i == ']' and top == '[':
                    stack = stack[0:-1]
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
