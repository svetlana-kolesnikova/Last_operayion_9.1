# from pandas.core.computation.common import result_type_many


# def create_counter():
#     count = [0]
#     def counter():
#         count[0] += 1
#         return str(*count)
#     return counter
#
#
# my_count = create_counter()
# print(my_count())
# print(my_count())
# print(my_count())
# print(my_count())
# print(my_count())

# from time import time
#
# from pandas.core.window.doc import kwargs_scipy


# def log(func):
#     def wrapper(*args, **kwargs):
#         time_1 = time()
#         print(f"Начало: {time_1}")
#         result = func(*args, **kwargs)
#         time_2 = time()
#         print(f"Конц: {time_2}")
#         print(f"Итого: {round(time_2 - time_1, 2)}")
#         return result
#     return wrapper

def digit_int(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        if type(result) == float:
            print("Stop")
            return round(result)

        elif type(result) in (list, tuple):
            # rounded = [round(x) if type(x) == float else x for x in result]
            for x in result:
                if type(x) == float:
                    rounded = round(x)
                else:

                    print("Stop")
            return type(result)(rounded)
        else:
            print("Stop")
            return result

    return wrapper

@digit_int
def func(a, b):
    summ_func = a + b
    return summ_func

print(func(60, 3))

# def exclamation_mark(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         if "!" in result:
#             return result.replace("!", "!!!")
#     return wrapper
#
# def question_mark(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         if "?" in result:
#             return result.replace("?", "???")
#     return wrapper
#
# def three_dots(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         if "." in result:
#             return result.replace(".", "...")
#     return wrapper
#
# @three_dots
# @question_mark
# @exclamation_mark
# def function():
#     return "Hello! World? In."
#
# print(function())
#
# from datetime import datetime
#
# # Получаем текущую дату и время
# current_time = datetime.now()
#
# # Форматируем дату и время в нужный формат
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
#
# # Открываем файл в режиме добавления (или создаем, если он не существует)
# with open("start_log.txt", "a") as file:
#     # Записываем дату и время в файл
#     file.write(f"Программа запущена в: {formatted_time}\n")

# if __name__ == '__main__':
    # @log
    # def example():
    #     for i in range(100000000):
    #         continue
    #
    # example()
