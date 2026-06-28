from itertools import permutations
def solution(numbers):
    answer = 0
    s = set()
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            s.add(int(''.join(p)))
    for num in s:
        if is_prime(num):
            answer += 1
    return answer

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True