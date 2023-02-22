fint = open('input.txt')
fout = open('output.txt', 'w')
x = fint.readline().split()
n = int(x[0])
m = int(x[1])
graph = [[] for i in range(n)]
for i in range(m):
    x = fint.readline().split()
    v = int(x[0])
    u = int(x[1])
    graph[v-1].append(u-1)


def dfs(v, u):
    for i in u:
        if graph[i] != [-1]:
            dfs(i, graph[i])
    sorted_graph.append(v+1)
    graph[v] = [-1]


sorted_graph = []
for i in range(n):
    if graph[i] != [-1]:
        dfs(i, graph[i])

sorted_graph.reverse()
fout.write(' '.join([str(i) for i in sorted_graph]))
