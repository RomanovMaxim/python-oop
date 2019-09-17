class Wrapper:

    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

if __name__ == '__main__':

    X = Wrapper([1, 2, 3])
    X.append(4)
    print(X.wrapped)

    X = Wrapper({'a':1, 'b':2})
    print(X.keys())
