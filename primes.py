from math import sqrt


def primes_list(start, end):
    """
     Принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
    """
    primes = []
    for i in range(start, end+1):
        for j in range(2, int(sqrt(i))+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
