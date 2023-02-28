"https://leetcode.cn/problems/valid-parentheses/"


class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for c in s:
            if c == "("  or c == "{"  or c == "["  :
                stack.append(c)
            else:
                if not stack:
                # if len(stack)==0:
                    return False
                elif c == ")"  and stack[-1] != "(":
                    return False
                elif c == "]"  and stack[-1] != "[":
                    return False
                elif c == "}"  and stack[-1] != "{":
                    return False
                stack.pop()
        
        if stack:
            return False
        else:
            return True
