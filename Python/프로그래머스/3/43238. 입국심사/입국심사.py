def solution(n, times):
    lo, hi = 1, min(times) * n
    answer = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if sum(mid // t for t in times) >= n:
            answer = mid      
            hi = mid - 1
        else:
            lo = mid + 1    
    return answer