from itertools import combinations

def parse_input():
    return [{
        'offset_y': int(_.split('@')[1].split(':')[0].split(',')[0].strip()),
        'offset_x': int(_.split('@')[1].split(':')[0].split(',')[1].strip()),
        'y': int(_.split('@')[1].split(':')[1].split('x')[0].strip()),
        'x': int(_.split('@')[1].split(':')[1].split('x')[1].strip()),
    } for _ in open('q3.txt', 'r').read().splitlines()]

def solve():
    rects = parse_input()
    overlaps = []
    id = 0
    for (a, b) in combinations(rects, 2):
        pass

