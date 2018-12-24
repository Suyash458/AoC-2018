import re
from collections import defaultdict

lines = sorted(open('q4.txt', 'r').read().splitlines())
times = defaultdict(lambda: [0] * 60)
id = None
start_time = 0

for line in lines:
    for (minute, entry) in re.findall(r'(\d+)](.*)', line):
        if entry.endswith('begins shift'):
            id = int(entry.strip().split(' ')[1][1::])
        if entry.endswith('falls asleep'):
            start_time = int(minute)
        if entry.endswith('wakes up'):
            if id:
                for i in range(start_time, int(minute)):
                    times[id][i] += 1

max_id = max([(id, sum(times[id])) for id in times], key=lambda x: x[1])
print(max_id[0] * times[max_id[0]].index(max(times[max_id[0]])))

max_id = max([(id, max(times[id])) for id in times], key=lambda x: x[1])
print(max_id[0] * times[max_id[0]].index(max(times[max_id[0]])))


