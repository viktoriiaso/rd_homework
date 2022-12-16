# 1. Створити програму, яка буде очікувати від користувача введення
# тексту і виведе інформацію по кожному надрукованому символу:
# це “число” + яке воно (парне, непарне),
# це “буква” + яка вона (велика чи маленька),
# це “символ”
word = input('enter something ')
for letter in word:
    if letter.isdigit():
        if int (letter) % 2 == 0:
            print(f'{letter} is a even')
        else:
            print(f'{letter} is odd')
    elif letter.isupper():
        print(f'{letter} is upper case')
    elif letter.islower():
        print(f'{letter} is lower case')
    else:
        print(f'{letter} is a symbol')

# 2. Створити програму, яка буде друкувати в консоль “I love Python” кожні 4.2 секунди,
# поки її виконання не буде перервано вручну.
# Підказка: для того, щоб програма могла зупинитися на вказаний час, можна використати
# бібліотеку time (import time), а саме функцію sleep().
# (time.sleep(second), де second, це кількість секунд, які програма має чекати).

import time
while True:
    time.sleep(4.2)
    print('i love Python')