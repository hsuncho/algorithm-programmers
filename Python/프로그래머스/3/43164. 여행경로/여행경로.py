def solution(tickets):
    tickets.sort()
    answer = ["ICN"]
    n = len(tickets)
    used = [False] * n
    
    def dfs(v):
        if len(answer) == n + 1:
            return True

        for i in range(n):
            if tickets[i][0] == v and not used[i]:
                used[i] = True
                answer.append(tickets[i][1])
                
                if dfs(tickets[i][1]):
                    return True
                
                used[i] = False
                answer.pop()
        return False
    
    dfs("ICN")
    return answer
