class Person:

    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def getlastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return f'<{self.__class__.__name__} => Name: {self.name}, Pay: {self.pay}>'
