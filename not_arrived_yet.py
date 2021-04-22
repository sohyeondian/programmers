def solution_inefficiency(participant, completion):
    for name in completion:
        participant.remove(name)
        # remove() -> (maybe) check "participant" list's all items = O(N)
    # O(N ** 2) = O(N): for * O(N): remove()
    answer = participant[0]
    return answer


def solution(participant, completion):
    # sort both lists => the same name in the same index
    # .sort() : O(N * logN)
    participant.sort()
    completion.sort()
    # for -> O(N) : just check only one time of "completion" list's items
    for i in range(len(completion)):
        print(participant[i], completion[i])
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(completion)]


print(solution(["leo", "kiki", "eden", "kiki"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))