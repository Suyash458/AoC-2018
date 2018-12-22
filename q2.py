from collections import Counter

def distance(a, b):
    diffs = 0
    diff_index = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_index = i
            diffs += 1
    if diffs == 1:
        print(a[0:diff_index] + a[diff_index+1::])

ids = open('q2.txt','r').read().splitlines()
unique_counts = [set(Counter(i).values()) for i in ids]
twos = len(list(filter(lambda x: 2 in x, unique_counts)))
threes = len(list(filter(lambda x: 3 in x, unique_counts)))

print(twos * threes)

for i, a in enumerate(ids):
    for b in ids[i+1::]:
        distance(a, b)