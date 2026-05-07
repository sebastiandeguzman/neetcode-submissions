class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isnumeric():
                stack.append(t)
            elif t[1:].isnumeric():
                stack.append(t)
            else:
                pop1 = int(stack.pop())
                pop2 = int(stack.pop())
                match t:
                    case "*":
                        stack.append(pop2 * pop1)
                    case "+":
                        stack.append(pop2 + pop1)
                    case "-":
                        stack.append(pop2 - pop1)
                    case "/":
                        stack.append(pop2 / pop1)
        return int(stack[0])
        

            