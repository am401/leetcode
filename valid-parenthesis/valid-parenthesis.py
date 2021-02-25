class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(','{','[']
        closed_brackets = [')','}',']']
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif i in closed_brackets:
                stack = stack[0:-1]
        if len(stack) == 0:
            return True
        else:
            return False
