class Solution:
    def isValid(self, s: str) -> bool:
        red=[]
        stackers= { '}': '{', ']': '[', ')' : '('}
        for c in s:
            if c in stackers:
                if red and red[-1]== stackers[c]:
                    red.pop()
                else:
                    return False
            else:
                red.append(c)

        return True if not red else False
#ive done this multiple times in uni wasnt that difficult just switching it from CPP to py