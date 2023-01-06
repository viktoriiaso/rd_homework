def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield b
        a, b = b, a + b
num = int(input('Enter some number '))
fib_list = (list(fib(num)))
print (fib_list[-1])