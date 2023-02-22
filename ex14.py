import queue


class Node:
    def __init__(self, time_1, time_2, node):
        self.node = node
        self.time_1 = time_1
        self.time_2 = time_2


fint = open('input.txt')
fout = open('output.txt', 'w')
n = int(fint.readline())
x = fint.readline().split()
start = int(x[0])-1
goal = int(x[1])-1
m = int(fint.readline())
graph = [[] for i in range(n)]
for i in range(m):
    x = fint.readline().split()
    v = int(x[0])-1
    time_1 = int(x[1])
    u = int(x[2])-1
    time_2 = int(x[3])
    graph[v].append(Node(time_1, time_2, u))


def bfs(node, goal):
    inf = 10**9
    time = [inf for i in range(n)]
    time[node] = 0
    q = queue.Queue()
    q.put([node, 0])

    while not q.empty():
        x = q.get()
        cur = x[0]
        cur_time = x[1]
        for i in graph[cur]:
            if i.time_2 < time[i.node] and i.time_1 >= cur_time:
                time[i.node] = i.time_2
                q.put([i.node, i.time_2])
    if time[goal] < inf:
        return time[goal]
    else:
        return -1


fout.write(str(bfs(start, goal)))
