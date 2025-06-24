class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c =='+':
                stack.append(stack.pop() +stack.pop())
            elif c=='-':
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c== '*':
                stack.append(stack.pop() *stack.pop())
            elif c== '/':
                a,b= stack.pop(),stack.pop()
                stack.append(int((b /a)))
            else:
                stack.append(int(c))
        return stack[0]

#again a uni problem i did, just had to remember the logic and do it in py instead of cpp. 