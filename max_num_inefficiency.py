from itertools import permutations


def solution(numbers):
    # find number of all cases using itertools.permutations
    all_joins = list(permutations(numbers, len(numbers)))
    # (int,) -> (str,) -> JOIN str
    all_joins = [''.join(list(map(str, x))) for x in all_joins]
    # maximum number to str (*for Restrictions*)
    answer = int(max(all_joins))
    return str(answer)


print(solution([0, 0, 0]))
print(solution([3, 30, 34, 5, 9]))
print(solution([21, 212]))
print(solution([34, 3, 307, 0]))  # 3430




