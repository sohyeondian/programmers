def solution(numbers):
    
    answer = ''
    return answer

    numbers = list(map(str, numbers))

    nums = quick(numbers)

    answer = int(''.join(nums))
    return str(answer)

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equar_arr, greater_arr = [], [], []
    for num in arr:
        if pivot == num:
            equar_arr.append(pivot)
        elif pivot + num > num + pivot:
            lesser_arr.append(num)
        else:
            greater_arr.append(num)

    return quick(greater_arr) + equar_arr + quick(lesser_arr)


print(solution([101, 1, 10]))  # 110110 101 > 10
print(solution([110, 100, 111, 1000]))
print(solution([212, 21, 2]))

print(solution([0, 0, 0]))
print(solution([3, 30, 34, 5, 9]))
print(solution([21, 212]))


print(solution([34, 3, 0]))  # 3430
print(solution([31, 3, 2]))  # 3312

print(sorted(['31', '3', '2'], reverse=True))
print('31' > '3')

print(solution([90,908,89,898,10,101,1,8,9]))
print(solution([1, 11, 111, 1111] ))
print(solution([10, 101]))
print(solution([0, 0, 0, 0, 0, 0]))
print(solution([8, 898, 89])) # 898988
