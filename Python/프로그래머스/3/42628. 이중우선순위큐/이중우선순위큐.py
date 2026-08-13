import heapq
def solution(operations):
    minh = []
    maxh = []
    deleted = set()
    idx = 0
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(minh, (num, idx))
            heapq.heappush(maxh, (-num, idx))
            idx += 1
        elif num == -1:
            while minh and minh[0][1] in deleted:
                heapq.heappop(minh)
            if minh:
                deleted.add(heapq.heappop(minh)[1])
        elif num == 1:
            while maxh and maxh[0][1] in deleted:
                heapq.heappop(maxh)
            if maxh:
                deleted.add(heapq.heappop(maxh)[1])
    
    while maxh and maxh[0][1] in deleted:
        heapq.heappop(maxh)
    while minh and minh[0][1] in deleted:
        heapq.heappop(minh)
    
    if minh and maxh:
        return [-maxh[0][0], minh[0][0]]
    else:
        return [0,0]