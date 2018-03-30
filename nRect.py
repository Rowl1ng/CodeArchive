import numpy as np
import networkx as nx

n = 4  # num of rects
x1 = [0, 100, 0, 100]
y1 = [0, 0, 100, 100]
x2 = [200, 300, 200, 300]
y2 = [200, 200, 300, 300]

blocks = np.zeros([n, 4])
for i in range(n):
    blocks[i] = [x1[i], y1[i], x2[i], y2[i]]


def intersects(rect1, rect2):
    return not (rect1[2] < rect2[0]
                or rect1[0] > rect2[2]
                or rect1[3] < rect2[1]
                or rect1[1] > rect2[3])


inters = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        if intersects(blocks[i], blocks[j]):
            inters[i, j] = 1
inters += inters.T - np.diag(inters.diagonal())
G = nx.from_numpy_matrix(inters)
results = list(nx.find_cliques(G))
lens = [len(result) for result in results]
answer = max(lens)
print answer