// https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # Addition operator: Add the 2 top values:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
                
            # Minus operator: subtract the 2 top values:
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
        
            # Multiplication operator: multiply the 2 top values:
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
                
            # Div operator: floor divide the 2 top values:
            elif token == "/": 
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
                
            # Otherwise just add to stack:
            else:
                stack.append(int(token))
                
        # Result will always be at the top of the stack:
        return stack[0]
