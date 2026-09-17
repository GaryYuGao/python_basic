from class_7_1_person import Person


class Manager(Person):
    """
    带有自定义加薪的Person
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveraise(self, percent, bonus=0.1):
        Person.giveraise(self, percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)

    print(tom.job)
    print(tom)
