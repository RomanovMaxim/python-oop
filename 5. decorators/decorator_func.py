# Реализация с помощью функции
def decorator(func):
    print('Вызов декоратора')
    def wrapper(*args):
        print(f'Вызов {func.__name__}{args}')
        print('Результат:', end=' ')
        return func(*args)
    return wrapper

@decorator
def myfunc(x, y):
    return x + y

@decorator
def glue_strings(*args):
    return ' '.join(args)

# Реализация с помощью класса
class decorator_class:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print('Вызов декоратора')
        return self.func(*args)

@decorator_class
def number(x, y, z):
    return str(x) + str(y) + str(z)

print(myfunc(66, 7))
print(glue_strings("Hello", ',', 'John', 'Connor'))
print(number(1,2,3))
