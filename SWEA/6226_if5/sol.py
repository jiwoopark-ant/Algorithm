import sys
sys.stdin = open ('input.txt',encoding='utf-8')

char=input()

if char.isupper():
    result=char.lower()
else:
    result=char.lower()

print(char, result)
print(ord(char), ord(result))