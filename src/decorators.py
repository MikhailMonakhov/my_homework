from functools import wraps
from time import time
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования"""

    def wrapper(function):
        """Функция декоратора, которая получает обозреваемую функцию и возвращает внутреннюю функцию inner"""

        @wraps(function)
        def inner(*args, **kwargs):
            """
            Внутренняя функция, которая передаёт аргументы для обозреваемой функции
            и сохраняет в указанном формате её результат
            """
            result = ""
            try:
                # замер и результат функции
                time_start = time()
                result = function(*args, **kwargs)
                time_stop = time()
                # сообщения для логов
                log_message_info = f"{function.__name__} ok\n"
                log_message_time = f"Time for work: {time_stop - time_start}\n"
                log_message = log_message_info + log_message_time
                # определение записи
                if filename in (None, "", " "):
                    print(log_message)
                else:
                    # отступ между логами
                    log_message += "\n"
                    # очень простая проверка на тип файла
                    if ".txt" in filename:
                        set_filename = filename
                    else:
                        set_filename = filename + ".log"
                    # запись в файл
                    with open(set_filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
            except Exception as error_type:
                # сообщение для логов
                log_error_message = f"{function.__name__} error: {type(error_type).__name__}. Inputs: {args}, {kwargs}"
                # определение записи
                if filename in (None, "", " "):
                    print(log_error_message)
                else:
                    # отступ между логами
                    log_error_message += "\n"
                    # очень простая проверка на тип файла
                    if ".txt" in filename:
                        set_filename = log_error_message
                    else:
                        set_filename = log_error_message + ".log"
                    # запись в файл
                    with open(set_filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_error_message)
                    raise error_type

            return result

        return inner

    return wrapper


@log("greetings")
@log("greetings.txt")
def hello_world():
    print("Hello, World!")

hello_world()