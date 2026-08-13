def solution(clothes):
    hash_map = {}
    
    for name, category in clothes:
        hash_map[category] = hash_map.get(category, 0) + 1
    answer = 1
    for cnt in hash_map.values():
        answer *= cnt + 1
    return answer - 1