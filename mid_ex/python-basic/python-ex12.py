class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        self.id = id

    def getID(self):
        print(self.id)


info = Employee("IoT", 65, 2018)
info.getID()
info.getName()
info.getAge()