def game_core_v3(number: int = 1) -> int:
    
    """В зависимости от того, больше или меньше загаданное число середины
    допустимого интервала, устанавливаем новое число в середине интервала.
    Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 0
    interval = 102
    while predict_number != number and count < 100:
        count += 1
        # print(count)
        interval = round(interval/2)
        # print(interval)
        if predict_number > number:
            predict_number -= interval
        elif predict_number < number:
            predict_number += interval
        # print(predict_number)
    return count

# for n in range(0, 101):
    # print(game_core_v3(n))

