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
        super().__init__(age, name)
        self.id = id

    def getId(self):
        print(self.id)


p1 = Employee("iot", 65, 2017)

p1.getAge()
p1.getName()
p1.getId()