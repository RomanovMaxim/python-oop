from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Создает и обрабатывает записи с информацией о людях
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __str__(self):
    #     return f'[{self.__class__.__name__}: {self.name}, {self.pay}]'


# 1 Manager наследует Person
class Manager(Person):
    """
    Версия класса Person, адаптированная в соответствии
    со специальными требованиями
    """

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mng', pay)

    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)


# 2 Manager НЕ наследует Person (это пример шаблона ДЕЛЕГИРОВАНИЕ)
# class Manager:
#
#     def __init__(self, name, pay):
#         self.person = Person(name, 'mng', pay)
#
#     def giveRaise(self, percent, bonus=0.1):
#         self.person.giveRaise(percent + bonus)
#
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)
#
#     def __str__(self):
#         return str(self.person)


class Department:

    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)
    print(sue)

    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.1)
    print(sue)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)

    # Полиморфизм
    print('-- All three --')
    for obj in (bob, sue, tom):
        obj.giveRaise(0.1)
        print(obj)


    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(0.1)
    development.showAll()
