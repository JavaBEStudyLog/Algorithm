def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge = [0] * bridge_length
    total_weight = 0

    for truck in truck_weights:
        while True:
            count += 1
            exited_truck = bridge.pop(0)
            total_weight -= exited_truck

            if total_weight + truck <= weight:
                bridge.append(truck)
                total_weight += truck
                break
            else:
                bridge.append(0)
    count += bridge_length

    return count