import os
from datetime import datetime

def logger(path):

    param_to_file = str

    def __logger(old_function):
        def new_function(*args, **kwargs):
            param_to_file = f'Дата и время вызова функции: {str(datetime.now())} \n'
            param_to_file += f'Аргументы: позиционные {args}; именованные {kwargs} \n'

            result = old_function(*args, **kwargs)

            param_to_file += f'Имя функции: {old_function.__name__} \n'
            param_to_file += f'Возвращаемый результат: {str(result)} \n'
            param_to_file += '\n'


            with open(path, 'a', encoding='utf-8') as file:
                file.write(param_to_file)

            return result

        return new_function

    return __logger