class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in "[{(":
                stack.append(bracket)
            else:
                if bracket in ")]}":
                    if len(stack) == 0:
                        return False
                    br = stack.pop() # now if nothing is in the stack or 
                    # the last element isnt the same then return False
                    if bracket == ")" and br != "(":
                        return False
                    elif bracket == "}" and br != "{":
                        return False
                    elif bracket == "]" and br != "[":
                        return False
                    
        return stack == []