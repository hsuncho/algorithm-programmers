def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        
        if remain % speeds[i] == 0:
            day = remain // speeds[i]
        else:
            day = remain // speeds[i] + 1
            
        days.append(day)
        
    cnt = 1
    standard = days[0]
    
    for i in range(1, len(days)):
        if days[i] <= standard:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            standard = days[i]
    answer.append(cnt)
    return answer