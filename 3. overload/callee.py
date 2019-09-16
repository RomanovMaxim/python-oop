class Callee:

    def __call__(self, *pargs, **kargs):
        print('Called:', pargs, kargs)


class Prod:

    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


if __name__ == '__main__':

    C = Callee()
    print(C(1, 2, 3))
    print(C(1, 2, 3, x=4, y=5))

    X = Prod(2)
    print(X(3))
    print(X(4))
