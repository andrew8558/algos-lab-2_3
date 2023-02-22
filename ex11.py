import queue


fint = open('input.txt')
fout = open('output.txt', 'w')
m = int(fint.readline())
graph = {}
for i in range(m):
    x = fint.readline().strip().split()
    v, u = x[0], x[2]
    if v in graph.keys():
        graph[v].append(u)
    else:
        graph[v] = [u]
    if u not in graph.keys():
        graph[u] = []

start = fint.readline().strip()
goal = fint.readline().strip()
if start not in graph.keys():
    graph[start] = []
if goal not in graph.keys():
    graph[goal] = []


def bfs(node, goal):
    inf = 10**9
    dist = {}
    for i in graph.keys():
        dist[i] = inf
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


fout.write(str(bfs(start, goal)))
