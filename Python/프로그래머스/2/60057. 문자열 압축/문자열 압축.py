def solution(s):
    answer = len(s)
    cnt = 1
    
    # 문자열 길이의 절반보다 큰 단위로 자르면 같은 문자열이 2번 이상 반복될 수 없음
    while cnt <= len(s) // 2:
        result = []
        pattern_cnt = 1
        pattern = s[0:cnt]
        for i in range(cnt, len(s), cnt):
            if s[i:i+cnt] == pattern:
                pattern_cnt += 1
            else:
                pattern = str(pattern_cnt) + pattern if pattern_cnt != 1 else pattern
                result.append(pattern)
                pattern = s[i:i+cnt]
                pattern_cnt = 1

        pattern = str(pattern_cnt) + pattern if pattern_cnt != 1 else pattern
        result.append(pattern)
        answer = min(answer, len(''.join(result)))
        cnt += 1
    return answer