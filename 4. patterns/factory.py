def factory(aClass, *args):
    return aClass(*args)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

if __name__ == "__main__":

    object1 = factory(Spam)
    object2 = factory(Person, "John", "savior")
