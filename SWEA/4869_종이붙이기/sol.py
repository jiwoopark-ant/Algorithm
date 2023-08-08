# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     sol = a(N//10)

#     print("#{} {}".format(tc, ans))

# def a(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     return a(n-1) + a(n-2) * 2



# Test_case=int(input())

# def function(N):
#     if N%10==0:
#         if N==10: #N=10일때 1반환
#             return 1
#         elif N==20: #20x20은 3반환 
#             return 3
#         else:
#             return function(N-10)+(2*function(N-20))
#     else:
#         print("10의 배수만 입력하세요")
import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

memo = [0, 1, 3]

for tc in range(1, T+1):
    N = int(input()) // 10

    # memo배열에 출력시킬 값이 없으면 추가
    while N >= len(memo):
        # n-2 배열에 가로로 작은 사각형 두개 쌓거나 큰 사각형 쌓는 방법 (x2)
        # n-1 배열에 세로로 작은 사각형 쌓는 방법 하나.
        temp = 2 * memo[len(memo)-2] + memo[len(memo)-1]
        memo.append(temp)

    print(memo[N])

