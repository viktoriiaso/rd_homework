#1. Створити програму, яка буде очікувати введення тексту від користувача
# і повідомляти — чи є введений текст “числом” чи “словом”.
#2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.
#3. Якщо це “слово”, програма має вказати його довжину

some_text = input('Enter some text')
print(type(some_text))

if some_text.isdigit():
    num = int(some_text)%2
    if num == 0:
        print('number is even')
    else:
        print('number is odd')
else:
    print(len(some_text))