def solution(answers):
    pattern1 = (1, 2, 3, 4, 5)
    pattern2 = (2, 1, 2, 3, 2, 4, 2, 5)
    pattern3 = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    scores = [0, 0, 0]
    for index in range(len(answers)):
        if answers[index] == pattern1[index % len(pattern1)]:
            scores[0] += 1
        if answers[index] == pattern2[index % len(pattern2)]:
            scores[1] += 1
        if answers[index] == pattern3[index % len(pattern3)]:
            scores[2] += 1
    maxi = max(scores)
    answer = []
    for num in range(len(scores)):
        if scores[num] == maxi:
            answer.append(num + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]