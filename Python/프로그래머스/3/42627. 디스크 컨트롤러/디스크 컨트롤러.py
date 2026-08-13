# 1. 작업들을 요청 시각 기준으로 정렬한다 (도착 순서대로 넣기 위해)
# 2. current_time = 0, 처리한 작업 수 = 0
# 3. 모든 작업을 처리할 때까지 반복:
#     a. 요청 시각 <= current_time 인 작업을 전부 힙에 넣는다
#     b. 힙이 비어있으면? → 아직 아무도 도착 안 함
#          → current_time을 다음 작업의 요청 시각으로 점프
#     c. 힙이 차있으면 → 가장 짧은 작업을 pop
#          → current_time += 그 작업의 소요시간
#          → 걸린 시간 += (current_time - 그 작업의 요청시각)

import heapq as hq
def solution(jobs):
    jobs.sort()
    n = len(jobs)
    current_time = 0
    total_time = 0
    cnt = 0
    idx = 0
    h = []
    
    while cnt < n:
        while idx < n and jobs[idx][0] <= current_time:
            hq.heappush(h, (jobs[idx][1], jobs[idx][0]))
            idx += 1
    
        if h:
            dur, req = hq.heappop(h)
            current_time += dur
            total_time += current_time - req
            cnt += 1
        else: # 대기 중인 작업이 없다면
            current_time = jobs[idx][0]
    return total_time // n