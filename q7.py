import re, heapq

instructions = open('q7.txt').read().splitlines()

completed = []
candidates = []
workers = [[None, None] for _ in range(5)]
jobs = {}

ticks = 0

def job_duration(job):
    return 60 + (ord(job) - ord('A') - 1)

def is_candidate(job):
    return all([(dep in completed) for dep in deps]) and job not in candidates + completed + [_[0] for _ in workers]

for instruction in instructions:
    for dep, job in re.findall(r'.* (.) .* (.) .*', instruction):
        if job not in jobs:
            jobs[job] = []
        if dep not in jobs:
            jobs[dep] = []
        jobs[job].append(dep)

while len(completed) != len(jobs):
    for i, job in enumerate(workers):
        if job[0] and job_duration(job[0]) == (job[1] - 1):
                completed.append(job[0])
                workers[i] = [None, None]
    for job, deps in jobs.items():
        if is_candidate(job):
            heapq.heappush(candidates, job)
    for i, job in enumerate(workers):
        if not job[0] and candidates:
                workers[i] = [heapq.heappop(candidates), 0]
        if job[0]:
            job[1] += 1
    ticks += 1

print(''.join(completed), ticks - 1)