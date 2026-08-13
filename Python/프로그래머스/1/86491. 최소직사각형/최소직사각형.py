def solution(sizes):
    long_side = max(max(w, h) for w, h in sizes)
    short_side = max(min(w, h) for w, h in sizes)
    return long_side * short_side