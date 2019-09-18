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


class Super:

    def __init__(self):
        print('Вызов конструктора')
        pass

    @decorator
    def method(self, x, y):
        print(x+y)


print(myfunc(66, 7))
X = Super()
X.method(5, 10)
