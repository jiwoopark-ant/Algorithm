T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sol = a(N//10)

    print("#{} {}".format(tc, ans))

def a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return a(n-1) + a(n-2) * 2



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

