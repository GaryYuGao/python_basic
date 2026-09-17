# 创建一个工资系统
class Person:
    def __init__(self, name, age, pay=0, job=None): #  初始化类实例的方法
        self.name = name #  self为实例
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software') #  产生实例
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name)
    print(sue.pay)

    print(bob.name.split()[-1]) #  查询Lastname
    sue.pay = int(sue.pay * 1.10) #  加薪
    print(sue.pay)
