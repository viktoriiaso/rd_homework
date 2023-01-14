# Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
# Декоратор має працювати для різних функцій однаково.

import time

def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.strftime("%H:%M:%S")
        func(*args, **kwargs)
        print("Start time: ", func.__name__, begin)
    return inner

@calculate_time
def add_numbers_(a, b):
    print(a+b)
add_numbers_(1,2)

# Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює перед виконанням коду та після виконання коду,
# таким чином виділяючи блок коду символами дорівнює.
# У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.

class ContextManagerDz():
    def __enter__(self):
        print('==========')
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('==========')

with ContextManagerDz() as manager:
    print('Some text')

# Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж, що і менеджер контексту із попереднього завдання.

try:
    print('==========')
except Exception as ex:
    print(f'some exception: {ex}')
else:
    print('do something')
finally:
    print('==========')

# Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".
class MyException(Exception):
    pass
raise MyException('Custom exception is occured')
