#인법행렬 방식으롤 그래프를 저장

sys.stdin = open (input_path)

T= int(input())
for tc in range(1, T+1):







while len(stack):

    now=stack.pop()
    check_list[now] = True 

    for link in range(V+1):


        if nodes[now][link]  == 1:

            if not xhecck_list[link]:
                if link == G :
                    result=1
                    stack.append(link)

 print(f'a{tc}{result}')                   