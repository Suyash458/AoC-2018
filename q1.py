from itertools import cycle

numbers = [int(i) for i in open('q1.txt', 'r').readlines()]
sums = set()
running_sum = 0

for i in cycle(numbers):
    running_sum += i    
    if running_sum in sums:
        print(running_sum)
        break
    sums.add(running_sum)
