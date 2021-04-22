def solution(numbers):
	# make int_list to string_list
    numbers = list(map(str, numbers))
    # using Quick Sort
    nums = quick(numbers)
    # join list to string & change to int because of '0'
    answer = int(''.join(nums))
    # answer must be String type
    return str(answer)

def quick(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    les, eqr, grt = [], [], []
    for num in nums:
        if pivot == num:
            eqr.append(pivot)
        # be aware every numbers are string type (ex.'30', '3')
        # need to checks (ex. '303' & '330')
        elif pivot + num > num + pivot:
            les.append(num)
        else:
            grt.append(num)

    return quick(grt) + eqr + quick(les)


print(solution([101, 1, 10]))  # 110110 101 > 10
print(solution([110, 100, 111, 1000]))
print(solution([212, 21, 2]))

print(solution([0, 0, 0]))
print(solution([3, 30, 34, 5, 9]))
print(solution([21, 212]))
print(solution([34, 3, 0]))  # 3430
print(solution([31, 3, 2]))  # 3312

print(solution([90,908,89,898,10,101,1,8,9]))
print(solution([1, 11, 111, 1111] ))
print(solution([10, 101]))
print(solution([0, 0, 0, 0, 0, 0]))
print(solution([8, 898, 89])) # 898988
