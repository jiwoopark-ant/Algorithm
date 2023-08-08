    for line in range(E):
        start, end= list(map(int, input().split()))
        nodes[start].append(end)

pprint(nodes)    


