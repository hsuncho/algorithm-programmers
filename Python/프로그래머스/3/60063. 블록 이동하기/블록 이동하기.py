from collections import deque
def solution(board):
    n = len(board)
    start = ((0, 0), (0, 1))
    time = 0
    
    visited = set()
    visited.add(start)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(start, time)])
    answer = 0
    
    while q:
        state, time = q.popleft()
        (x1, y1), (x2, y2) = state
        
        if (x1 == n-1 and y1 == n-1) or (x2 == n-1 and y2 == n-1):
            return time
        
        # 상하좌우 이동
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            
            next_state = tuple(sorted([(nx1, ny1), (nx2, ny2)]))
            
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and next_state not in visited:
                    visited.add(next_state)
                    q.append((next_state, time + 1))
            
        # 회전하는 경우
        if (x1 == x2): # 가로
            for d in [-1, 1]:
                if 0 <= x1 + d < n and board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                    next_state1 = tuple(sorted([(x1, y1), (x1 + d, y1)]))
                    next_state2 = tuple(sorted([(x2, y2), (x2 + d, y2)]))
                        
                    if next_state1 not in visited:
                        visited.add(next_state1)
                        q.append((next_state1, time + 1))
                    if next_state2 not in visited:
                        visited.add(next_state2)
                        q.append((next_state2, time + 1))
                    
        if (y1 == y2): # 세로
            for d in [-1, 1]:
                if 0 <= y1 + d < n and board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                    next_state1 = tuple(sorted([(x1, y1), (x1, y1 + d)]))
                    next_state2 = tuple(sorted([(x2, y2), (x2, y2 + d)]))
                    
                    if next_state1 not in visited:
                        visited.add(next_state1)
                        q.append((next_state1, time + 1))
                    if next_state2 not in visited:
                        visited.add(next_state2)
                        q.append((next_state2, time + 1))