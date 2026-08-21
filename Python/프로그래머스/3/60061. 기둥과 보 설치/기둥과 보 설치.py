answer = []

def check_collumn(x, y):
    if y == 0:
        return True
    if [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
        return True
    return False

def check_beam(x, y):
    if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
        return True
    return False

def check_all():
    for x, y, a in answer:
        if a == 0:
            if not check_collumn(x, y):
                return False
        elif a == 1:
            if not check_beam(x, y):
                return False
    return True

def solution(n, build_frame):
    for x, y, a, b in build_frame:
        if a == 0: # 기둥
            if b == 0: # 삭제
                answer.remove([x, y, 0])
                if not check_all():
                    answer.append([x, y, 0])
            elif b == 1 and check_collumn(x, y): # 설치
                answer.append([x, y, 0])
        else: # 보
            if b == 0: # 삭제
                answer.remove([x, y, 1])
                if not check_all():
                    answer.append([x, y, 1])
            elif b == 1 and check_beam(x, y): # 설치
                answer.append([x, y, 1])
    answer.sort()
    return answer