class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we have to clear the stack all the time
        # then we can just use eval 
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                # now token is an operator
                # and there are 2 numbers
                first = stack.pop()
                second = stack.pop()
                answer = int(eval(f"{second} {token} {first}"))
                stack.append(answer)
        return int(stack[0])