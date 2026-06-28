def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            score[0] += 1
        if answers[i] == s2[i % len(s2)]:
            score[1] += 1
        if answers[i] == s3[i % len(s3)]:
            score[2] += 1
    answer = []
    for i in range(3):
        if score[i] == max(score):
            answer.append(i+1)
    return answer