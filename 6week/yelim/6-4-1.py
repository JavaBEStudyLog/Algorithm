from itertools import product

DISCOUNTS = [10, 20, 30, 40]


def solution(users, emoticons):
    answer = [-1, -1]
    for discounts in product(DISCOUNTS, repeat=len(emoticons)):
        imo_plus, total_price = 0, 0
        for user in users:
            user_price = sum(
                [
                    (v * (1 - k / 100))
                    for k, v in zip(discounts, emoticons)
                    if k >= user[0]
                ]
            )
            if user_price >= user[1]:
                imo_plus += 1
            else:
                total_price += user_price
        if imo_plus < answer[0]:
            continue
        if answer[0] == imo_plus and total_price < answer[1]:
            continue
        answer = [imo_plus, total_price]

    return answer
