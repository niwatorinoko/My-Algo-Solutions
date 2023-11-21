class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            elif i[0] == "-" and len(i) >= 2:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                print(a,i,b)
                if i == '+':
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack.pop()