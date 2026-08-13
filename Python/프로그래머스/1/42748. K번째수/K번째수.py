def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer