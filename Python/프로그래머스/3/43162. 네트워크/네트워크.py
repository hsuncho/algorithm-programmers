from collections import deque
def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            answer += 1
            q = deque([i])
            visited[i] = True
            
            while q:
                current = q.popleft()
                for j in range(n):
                    if computers[current][j] == 1 and not visited[j]:
                        visited[j] = True
                        q.append(j)
    return answer