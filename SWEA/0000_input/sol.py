import sys 
sys.stdin= open('input.txt')

# N= int(input())

# print(N)

# if N%2==1:
#     print('홀수')
# else:
#     print('짝수')    

#     = int(input())

# print(N)

# if N%2==1:
#     print('홀수')
# else:
#     print('짝수')    

TC= int(input())
N=int(input())
for i in range(TC):
    
    if N%2==1:
         print('홀수')
    else:
         print('짝수')  

# 1타원 리스트
numbers=list(map(int, input().split()))
print(numbers)
for i in numbers:
     int_num=int(i) 

     if int_num % 2 == 1:
          print(f'{int_num}은 홀수입니다')


#2차원 리스트 input 받기
N= int(input())
matrix=[]

for i in range(N):
     numbers= list(map(int,input().split()))
     matrix.append(numbers)

print(matrix)    

for m in matrix:
     print(m)


#numbers= map ( int, input().split() )
