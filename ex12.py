fint = open('input.txt')
fout = open('output.txt', 'w')
x = fint.readline().split()
n = int(x[0])
m = int(x[1])


class Room:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour


graph = [[] for i in range(n)]
for i in range(m):
    x = [int(i) for i in fint.readline().strip().split()]
    graph[x[0]-1].append(Room(x[1]-1, x[2]))
    graph[x[1]-1].append(Room(x[0]-1, x[2]))

length = fint.readline()
route = [int(i) for i in fint.readline().split()]


cur_room = 0
x = 0
for i in route:
    for room in graph[cur_room]:
        if room.colour == i:
            cur_room = room.number
            break
    else:
        x = 'INCORRECT'
        break

if x:
    fout.write(x)
else:
    fout.write(str(cur_room+1))
