class ListInstance:
    """
    Примесный класс, реализующий получение форматированной строки при вызове
    функций print() и str() с экземпляром в виде аргумента, через наследование
    метода __str__, реализованного здесь; отображает только атрибуты
    экземпляра; self – экземпляр самого нижнего класса в дереве наследования;
    во избежание конфликтов с именами атрибутов клиентских классов использует
    имена вида __X
    """

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}: \n{self.__attrnames()}>'

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\tname {attr}={self.__dict__[attr]}\n'
        return result


class Spam(ListInstance):
     def __init__(self):
         self.firstname = 'John'
         self.lastname = 'Connor'


class ListInherited:
    """
    Использует функцию dir() для получения списка атрибутов самого экземпляра
    и атрибутов, унаследованных экземпляром от его классов; в Python 3.0
    выводится больше имен атрибутов, чем в 2.6, потому что классы нового стиля
    в конечном итоге наследуют суперкласс object; метод getattr() позволяет
    получить значения унаследованных атрибутов, отсутствующих в self.__dict__;
    реализует метод __str__, а не __repr__, потому что в противном случае
    данная реализация может попасть в бесконечный цикл при выводе связанных
    методов!
    """

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:' \
               f' \n{self.__attrnames()}>'

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += f'\tname {attr}=<>\n'
            else:
                result += f'\tname {attr}={getattr(self, attr)}\n'
        return result


class ListTree:
    """
    Примесный класс, в котором метод __str__ просматривает все дерево классов
    и составляет список атрибутов всех объектов, находящихся в дереве выше
    self; вызывается функциями print(), str() и возвращает сконструированную
    строку со списком; во избежание конфликтов с именами атрибутов клиентских
    классов использует имена вида __X; для рекурсивного обхода суперклассов
    использует выражение-генератор
    """

    def __str__(self):
        self.__visited = {}
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:' \
               f' \n{self.__attrnames(self, 0)}{self.__listclass(self.__class__, 4)}>'

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return f'\n{dots}<Class {aClass.__name__}:,'     \
                   f' address {id(aClass)}: (see above)>\n'
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            ga = ''.join(genabove)
            return f'\n{dots}<Class {aClass.__name__}, address {id(aClass)}:' \
                   f'\n{self.__attrnames(aClass, indent)}{ga}{dots}'

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + f'{attr}=<>\n'
            else:
                result += spaces + f'{attr}={getattr(obj, attr)}\n'
        return result




if __name__ == '__main__':

    x = Spam()
    print(x)
