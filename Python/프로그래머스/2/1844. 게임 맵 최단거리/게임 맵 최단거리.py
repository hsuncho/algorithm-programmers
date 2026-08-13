# 1. 거리 배열 준비
# 2. 큐에 시작점 (0,0) 넣기, 거리 1로 초기화
#    (칸 수를 세므로 시작칸도 1로 침)
# 3. 큐가 빌 때까지 반복:
#    a. 큐에서 (r, c) 하나 꺼내기
#    b. 네 방향 이웃 (nr, nc)에 대해:
#       - 지도 범위 안이고
#       - 길(1)이고
#       - 아직 방문 안 했으면
#       → 거리 = 현재칸 거리 + 1 로 기록
#       → 큐에 (nr, nc) 넣기
# 4. 도착점 (n-1, m-1)의 거리를 반환 (0이면 못 감 → -1)

from collections import deque
def solution(maps):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    q = deque()
    q.append((0,0))
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c] + 1
                q.append((nr, nc))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1