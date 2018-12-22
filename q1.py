from itertools import cycle

numbers = [int(i) for i in open('q1.txt', 'r').readlines()]
sums = set()
running_sum = 0

for i in cycle(numbers):
    if running_sum + i in sums:
        print(running_sum + i)
        break
    sums.add(running_sum + i)
    running_sum += i