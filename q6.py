from collections import defaultdict, Counter

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

coordinates = [(int(_.split(',')[0].strip()), int(_.split(',')[1].strip())) for _ in open('q6.txt', 'r').read().splitlines()]

grid = defaultdict(lambda: None)

for i, point in enumerate(coordinates):
    grid[point] = i

max_x = max(coordinates, key=lambda x: x[0])[0]
max_y = max(coordinates, key=lambda x: x[1])[1]
min_x = min(coordinates, key=lambda x: x[0])[0]
min_y = min(coordinates, key=lambda x: x[1])[1]

safe_region = 0
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        distances = [distance((x, y), point) for point in coordinates]
        if (x, y) not in coordinates:
            distances = [distance((x, y), point) for point in coordinates]
            min_dist = min(distances)
            if distances.count(min_dist) == 1:
                grid[(x, y)] = distances.index(min_dist)
        if sum(distances) < 10000:
            safe_region += 1

edges = set()
for x in range(min_x, max_x+1):
    edges.add(grid[(x, min_y)])
    edges.add(grid[(x, max_y)])

for y in range(min_y, max_y+1):
    edges.add(grid[min_x, y])
    edges.add(grid[max_x, y])

cells = Counter(grid.values())

print(max([size for (i, size) in cells.most_common() if i not in edges]))

print(safe_region)
