from collections import deque
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    def is_adjacent(a, b):
        diff = sum(1 for x, y in zip(a, b) if x != y)
        return diff == 1
    
    visited = set()
    queue = deque([(begin, 0)])
    visited.add(begin)
    
    while queue:
        current, step = queue.popleft()
        
        if current == target:
            return step
        
        for word in words:
            if word not in visited and is_adjacent(current, word):
                visited.add(word)
                queue.append((word, step + 1))

    return 0