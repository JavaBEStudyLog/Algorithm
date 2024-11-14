def solution(number, k):

    numbers = list(map(int,number))
    answer = ''
    last = len(numbers) - k

    for i in range(len(numbers) - k):

        last -= 1
        max_value = max(numbers[:len(numbers)-last])
        max_idx = numbers.index(max_value)
        answer += str(max_value)
        numbers = numbers[max_idx+1:]


    return answer