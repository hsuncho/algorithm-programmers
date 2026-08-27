from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    graph = [[0] * 102 for _ in range(102)]
    rectangles = []
    
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        rectangles.append((x1, y1, x2, y2))
    
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                graph[x][y] = 1
                
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                graph[x][y] = 0
                
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    queue = deque()
    queue.append((characterX, characterY, 0))
    
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX][characterY] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == itemX and y == itemY:
            return dist // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 102 or ny < 0 or ny >= 102:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))