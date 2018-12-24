from collections import Counter

def parse_input():
	return [{
		'id': int(_.split('@')[0][1::].strip()),
		'offset_y': int(_.split('@')[1].split(':')[0].split(',')[0].strip()),
		'offset_x': int(_.split('@')[1].split(':')[0].split(',')[1].strip()),
		'y': int(_.split('@')[1].split(':')[1].split('x')[0].strip()),
		'x': int(_.split('@')[1].split(':')[1].split('x')[1].strip()),
	} for _ in open('q3.txt', 'r').read().splitlines()]


def solve():
	rects = parse_input()
	mat = Counter()
	claim_ids = []
	for rect in rects:
		for x in range(rect['offset_x'], rect['offset_x'] + rect['x']):
			for y in range(rect['offset_y'], rect['offset_y'] + rect['y']):
				mat[(x, y)] += 1
	for rect in rects:
		if all((mat[(x, y)] == 1 for x in range(rect['offset_x'], rect['offset_x'] + rect['x']) for y in range(rect['offset_y'], rect['offset_y'] + rect['y']))):
			claim_ids.append(rect['id'])
	overlap = sum(map(lambda x: x > 1, mat.values()))
	print(overlap)
	print(claim_ids)

solve()