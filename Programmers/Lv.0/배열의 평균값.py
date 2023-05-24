def solution(numbers):
    answer = 0
    sum_nums = 0
    for i in numbers:
        sum_nums += i
    answer = sum_nums / len(numbers)
    return answer