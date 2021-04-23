from collections import deque


def solution(bridge_length, weight, truck_weights):
    on_bridge = deque()
    truck = deque(truck_weights)

    time = 0
    while on_bridge or truck:
        time += 1
        if on_bridge:
            for i in range(len(on_bridge)):
                on_bridge[i][1] += 1
            if on_bridge[0][1] > bridge_length:
                cur_weight = on_bridge.popleft()[0]
                weight += cur_weight

        if truck and truck[0] <= weight:
            on_bridge.append([truck.popleft(), 1])
            weight -= on_bridge[-1][0]

    return time