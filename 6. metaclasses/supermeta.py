class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call:', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)


class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


class Eggs:
    pass


print('making class')
class Spam(Eggs, metaclass=SubMeta):
    data = 1
    def meth(self, arg):
        pass


print('making instance')
X = Spam()
print('data:', X.data)
