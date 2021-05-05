﻿def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        elif char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return 1 if not stack else 0