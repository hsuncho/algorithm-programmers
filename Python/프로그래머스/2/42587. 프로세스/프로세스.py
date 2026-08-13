def solution(priorities, location):
    queue = []
    answer = 0
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    while queue:
        current = queue.pop(0)
        
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            
            if current[0] == location:
                return answer