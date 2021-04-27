def solution(bridge_length, weight, truck_weights):
    time = 0
    # If the list is empty OR the first truck exceeds the bridge's tolerable weight
    if not truck_weights or truck_weights[0] > weight:
        return time
    # on_bridge, times : using as QUEUE
    on_bridge = [truck_weights[0]]
    # times : for checking each truck's times on the bridge
    times = [1]
    # for next truck's weight
    next_index = 1
    time += 1
    # total weight of the trucks on the bridge
    total = truck_weights[0]
    while on_bridge:
        # if there is not next truck OR the next truck exceeds the bridge's tolerable weight
        if next_index >= len(truck_weights) or truck_weights[next_index] > weight:
            break
        times = [t + 1 for t in times]
        # pop first truck (QUEUE) -> minus total weight
        if times[0] > bridge_length:
            total -= on_bridge.pop(0)
            times.pop(0)
        # if total weight plus next truck's weight is okay for the bridge
        if total + truck_weights[next_index] <= weight:
            on_bridge.append(truck_weights[next_index])
            total += truck_weights[next_index]
            times.append(1)
            next_index += 1
        time += 1

    # if queue is not empty -> need to check last truck's time on the bridge
    if times:
        time += bridge_length - times[len(times) - 1] + 1

    return time


print('answer :', solution(2, 10, [7, 4, 5, 6]))  # 8
print('answer :', solution(100, 100, [10]))  # 101
print('answer :', solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
print('answer :', solution(2, 10, [10, 12]))