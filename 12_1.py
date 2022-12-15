from collections import defaultdict
from collections import deque
with open('input12.txt','r') as file:
#with open('input12-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

def shortest_path_unweighted(edges, start, end):
    # use breadth-first search
    # edges is a dict mapping each edge to a list of its neighbours
    visited = set()
    to_visit = deque([[start, 0]])
    while len(to_visit) > 0:
        curr, dist = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            for neighbour in edges[curr]:
                if neighbour == end:
                    return dist + 1
                if neighbour not in visited:
                    to_visit.append([neighbour, dist + 1])
    return np.inf

alphabet = 'abcdefghijklmnopqrstuvwxyz'
hillMap=[]
for line in lines:
    hillMap.append([char for char in line])

#arr = parse_multi_string(sep="")

# convert array to numeric
for i in range(len(hillMap)):
    for j in range(len(hillMap[0])):
        if hillMap[i][j] == "S":
            start = (i, j)
            hillMap[i][j] = "a"
        elif hillMap[i][j] == "E":
            end = (i, j)
            hillMap[i][j] = "z"
        hillMap[i][j] = alphabet.index(hillMap[i][j])

edges = defaultdict(list)
for i in range(len(hillMap)):
    for j in range(len(hillMap[0])):
        for [x, y] in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
            if (x >= 0) and (x < len(hillMap)) and (y >= 0) and (y < len(hillMap[0])) and (hillMap[x][y] - hillMap[i][j] <= 1):
                edges[i, j].append((x, y))

print(shortest_path_unweighted(edges, start, end))

