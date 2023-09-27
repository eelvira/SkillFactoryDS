"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1, predict_list: list = range(0, 101)) -> int:
    """Угадываем число, учитывая информацию о том,
    больше или меньше случайное число нужного нам числа.
    Функция принимает загаданное число и возвращает число попыток.
    Функция отрабатывает, если загаданное число находится в списке.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        predict_list (list, optional): Отсортированный список.
        Defaults список целых чисел от 0 до 100 включительно.
    Returns:
        int: Число попыток
    """
    count = 0
    low = 0
    high = len(predict_list) - 1

    while True:
        count += 1
        middle = low + (high - low) // 2
        predict_number = predict_list[middle]

        if number == predict_number:
            break  # выход из цикла если угадали

        elif number < predict_number:
            high = middle - 1

        elif number > predict_number:
            low = middle + 1

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов
    угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    # фиксируем сид для воспроизводимости
    np.random.seed(1)

    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
