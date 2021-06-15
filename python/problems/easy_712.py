"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def solve_easy_712(brackets):
    stack = []
    if not isinstance(brackets,str):
        raise ValueError("The input is not a string")
    for elm in brackets:
        if stack:
            if (stack[len(stack)-1] == "(" and elm == ")") or (stack[len(stack)-1] == "{" and elm == "}") or (stack[len(stack)-1] == "[" and elm == "]"):
                stack.pop()
            else:
                stack.append(elm)
        else:
            stack.append(elm)
    if not stack:
        return True
    return False




