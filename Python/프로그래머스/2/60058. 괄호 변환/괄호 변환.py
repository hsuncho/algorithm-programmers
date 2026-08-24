def divide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i + 1]
            v = p[i + 1:]
            return u, v

def check(s):
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0 :
            return False
        
    return cnt == 0

def solution(p):
    if not p:
        return ''
    
    u, v = divide(p)
    if check(u): # 올바른 문자열이라면
        return u + solution(v)
    
    answer = '('
    answer += solution(v)
    answer += ')'
    
    for ch in u[1: -1]:
        if ch == '(':
            answer += ')'
        else:
            answer += '(' 
    return answer