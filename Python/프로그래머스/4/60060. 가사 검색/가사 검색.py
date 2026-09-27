from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    right_idx = bisect_right(arr, right_value)
    left_idx = bisect_left(arr, left_value)
    return right_idx - left_idx

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
        
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    
    for q in queries:
        l = len(q)
        rq = q[::-1]
        if q[0] != '?':
            result = count_by_range(arr[l], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            result = count_by_range(reversed_arr[l], rq.replace('?', 'a'), rq.replace('?', 'z'))
        answer.append(result)
    return answer