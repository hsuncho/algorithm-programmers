def solution(N, stages):
    count = [0] * (N + 2)
    for s in stages:
        count[s] += 1
        
    users = len(stages)
    failure = []
    for stage in range(1, N + 1):
        if users == 0:
            failure.append((stage, 0))
        else:
            failure.append((stage, count[stage] / users))
        users -= count[stage]
        
    failure.sort(key = lambda x: (-x[1], x[0]))
    return [stage for stage, rate in failure]