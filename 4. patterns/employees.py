class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + self.salary * percent

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return f'<Employee: name={self.name}, salary={self.salary}>'


class Chef(Employee):

    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "makes food")

class Server(Employee):

    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, "interface with customer")

class PizzaRobot(Chef):

    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")

if __name__ == '__main__':

    Bob = PizzaRobot('Bob')
    print(Bob)
    Bob.work()
    Bob.giveRaise(0.20)
    print(Bob);  print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
