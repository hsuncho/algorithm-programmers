def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    foods = []
    for i in range(len(food_times)):
        foods.append((food_times[i], i + 1))
    foods.sort(key = lambda x: x[0])
    
    previous = 0
    stop_idx = 0
    for i in range(len(foods)):
        remains = len(foods) - i # 이 구간에 남아 있는 음식의 개수
        current = foods[i][0]
        time = (current - previous) * remains
        if time > k: # 이 구간에서 끝남
            stop_idx = i
            break
        k -= time
        previous = current
    
    rest = sorted(foods[stop_idx:], key=lambda x: x[1])
    return rest[k % remains][1]