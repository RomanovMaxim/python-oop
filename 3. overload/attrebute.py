class Empty:

    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


class AccessControl:

    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')


if __name__ == '__main__':

    X = Empty()
    print(X.age)
    #print(X.name)  # AttributeError

    Y = AccessControl()
    Y.age = 40
    print(Y.age)
    Y.name = 'John Connor'  # AttributeError
