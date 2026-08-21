from itertools import permutations
def solution(n, weak, dist):
    length = len(weak)
    weak = weak + [w + n for w in weak]
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in permutations(dist):
            cnt = 1
            position = weak[start] + friends[0]
            
            for idx in range(start, start + length):
                if weak[idx] > position:
                    cnt += 1
                    
                    if cnt > len(dist):
                        break
                        
                    position = weak[idx] + friends[cnt - 1]
                    
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1       
    return answer