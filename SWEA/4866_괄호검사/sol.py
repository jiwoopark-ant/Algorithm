# T = int(input())

# for t in range(T):
#     text = input()
#     stack = []
#     for i in text:
#         if i == "{" or i == "(":
#             stack.append(i)
#         elif stack and i == "}" and stack[-1] == "{":
#             stack.pop()
#         elif stack and i == ")" and stack[-1] == "(":
#             stack.pop()
#         elif i == "}" or i == ")":
#             stack.append(i)

#     if len(stack) == 0:               # stack의 길이가 0이 아님 : 오답
#         answer = 1          
#     else:                   # stack의 길이가 0 : 정답
#         answer = 0          

#     print(f"#{t+1}", answer)

import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    code = input()
    stack = []

    for char in code:
        if char == '(' or char == '{'
            stack.append(char)
        elif len(stack) and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if len(stack) == 0:
        result = 1
    else:
        result = 0