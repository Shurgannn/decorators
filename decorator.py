import random
import time


def dec_logger(path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            logger = old_function(*args, **kwargs)
            date_time = time.ctime()
            name = old_function.__name__
            arguments = locals()['args']
            with open(path, 'a', encoding='utf-8') as fw:
                fw.write(f'дата и время вызова функции - {date_time} \n'
                         f'имя функции - {name} \n'
                         f'аргументы, с которыми вызвалась функция - {arguments} \n'
                         f'возвращаемое значение - {logger} \n')
            return logger, date_time, arguments
        return new_function
    return decorator


@dec_logger('C:/My documents/decorators/text.txt')
def people():
    number = input('Введите номер документа')
    for people in documents:
        if people["number"] == number:
            print('Имя человека, которому принадлежит данный документ -', people["name"])
            return
        else:
            print('Такого номера документа нет в базе.')


@dec_logger('C:/My documents/decorators/text.txt')
def pow(lenght_list, start, end):
    random_list = [random.randrange(start, end) for _ in range(lenght_list)]
    return random_list


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

result1 = pow(10, 1, 10000)
result2 = people()