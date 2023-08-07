# T=int(input())

# for test_case in range(1,T+1):
#     #K: 최대 이동 가능 수
#     #N: 종점
#     #M: 충전기 정류장 수
#     K, N, M =map(int,input().split())

#     #charge:충전기 위치
#     charge=list(map(int,input().split()))+[N+K,N+K] #N+K리스트를 2개 추가해주는 이유는 밑에 while문에서 마지막 값이 범위를 벗어나기 때문에 만들어준것이다.
    
#     #현재 위치
#     here=0

#     #정류장 위치
#     i=0

#     #충전 할때마다 +1
#     cnt=0

#     while here +K<N: #현재위치에서 최대 이동가능한 만큼 이동했을때 종점보다 작을때 동안!
#         if here+K>=charge[i+2]: #만약에 현재위치에서 최대 이동가능한 만큼 이동한 게 충전소 위치의+2보다 크다면
#             here = charge[i+2] #현재 위치가 그 충전소 위치가 되고
#             cnt+=1             #충전을 한번 해주고
#             i+=3               #정류장 위치를 3만큼 더해준다.
#             continue

#         elif here+K >= charge[i+1]: #또한 만약에 현재위치에서 최대 이동가능한 만큼 이동한 것이 충전소 위치+1보다 크거나 같으면
#             here = charge[i+1]      #현재 위치가 그 충전소 위치가 되고
#             cnt+=1                  #충전을 한번 해주고
#             i+=2                    #정류장 위치를 2만큼 더해준다.
#             continue

#         elif here+K < charge[i]:     #또한 만약에 현재위치에서 최대 이동가능한 만큼 이동한 것이 충전소 위치보다 작으면
#             cnt=0                    #충전을 할 수 없으므로 cnt를 0으로 해준다. 
#             break                    #그리고 더 이상 움직일 수 없다.

#         else: 
#             here = charge[i]           #나머지 경우는 현재위치와 충전소 위치를 같게 해주고
#             cnt +=1                    #충전을 한번 해주고
#             i+=1                       #정류장 위치를 한번 더해준다.


#     print("#%d %d"%(test_case,cnt))


T = int(input())

for tc in range(1, T+1):
   
    K, N, M = map(int, input().split())
    charge_spot = list(map(int, input().split()))

    
    # 
    
    now = 0
    cnt = 0


  while n+