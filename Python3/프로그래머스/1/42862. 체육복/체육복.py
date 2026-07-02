# 1) 여벌이 있지만 본인도 도난당한 경우
# 2) 남은 여벌 보유자가, 앞 번호부터 도난 학생에게 빌려줌

def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    answer = n - len(lost_set)
    for r in sorted(reserve_set):
        if r-1 in lost_set:
            lost_set.remove(r-1)
            answer += 1
        elif r+1 in lost_set:
            lost_set.remove(r+1)
            answer += 1
    
    return answer