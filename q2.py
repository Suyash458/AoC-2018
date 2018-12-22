from collections import Counter

ids = [set(Counter(i).values()) for i in open('q2.txt','r').readlines()]

twos = len(list(filter(lambda x: 2 in x, ids)))
threes = len(list(filter(lambda x: 3 in x, ids)))

print(twos * threes)