def rotate_by_90_degree(key):
    row = len(key)
    col = len(key)
    result = [[0] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            result[c][row - r - 1] = key[r][c]
    return result

def check(new_lock):
    lock_len = len(new_lock) // 3
    
    # 중앙에 위치한 자물쇠의 n ~ 2n - 1 범위만 확인
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
        
    # 4가지 방향 확인
    for rotation in range(4):
        key = rotate_by_90_degree(key)
        
        # 한 칸씩 이동하며 자물쇠와 열쇠 비교
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False