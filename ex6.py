import queue


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
    graph[u-1].append(v-1)
x = fint.readline().split()
u = int(x[0])-1
v = int(x[1])-1


def bfs(node, goal):
    inf = 10**9
    dist = [inf for i in range(n)]
    dist[node] = 0
    q = queue.Queue()
    q.put(node)

    while not q.empty():
        cur = q.get()
        for i in graph[cur]:
            if dist[i] == inf:
                dist[i] = dist[cur] + 1
                q.put(i)
    if dist[goal] < inf:
        return dist[goal]
    else:
        return -1


fout.write(str(bfs(v, u)))
