class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import ast

        operators = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(int(a/b))
            else:
                stack.append(int(token))
        return stack[-1]