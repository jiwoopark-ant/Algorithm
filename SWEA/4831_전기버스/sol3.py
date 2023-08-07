import sys
sys.stdin = open('input.txt')

T=int(input())

for tc for range(1,T+1):
    #K 최대이동 가능 정류장
    #N 종점
    #M 중전기 설치 정류장 수
    K , N, M = map(int,input().split())

    bus_stop = list(map(int, input().split()))

    count=0
    #충전할 필요가 없이 바로 도착하눈 경우
    if K>= N :
         count=0
    else:
         pass

    print(f'#{tc}{count}')
    
