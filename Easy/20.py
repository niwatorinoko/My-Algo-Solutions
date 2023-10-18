class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif i == ')' and len(stack) != 0:
                if '(' == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            elif i == '}' and len(stack) != 0:
                if '{' == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            elif i == ']' and len(stack) != 0:
                if '[' == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
                
        if len(stack) == 0:
            return True
        return False