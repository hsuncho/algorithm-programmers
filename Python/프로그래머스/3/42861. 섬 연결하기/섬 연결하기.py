def solution(n, costs):
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    costs.sort(key = lambda x: x[2])
    answer = 0
    edges = 0
    for a, b, w in costs:
        roota, rootb = find(a), find(b)
        if roota != rootb:
            parent[roota] = rootb
            answer += w
            edges += 1
            if edges == n-1:
                break
    return answer