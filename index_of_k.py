def solution(array, commands):
    answer = []
    for com in commands:
        # com[0] start, [1] end -> sort -> index[2]
        tmp = sorted(array[com[0] - 1:com[1]])
        answer.append(tmp[com[2]-1])
    return answer


result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(result)