import sys
sys.stdin = open ('input.txt',encoding='utf-8')

a=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {
    'A' :0,
    'B':0,
    'O':0,
    'AB':0
}


for blood in a:
    dic[blood] +=1

print(dic)    