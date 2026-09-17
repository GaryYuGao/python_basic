from class_2_person_2_add_action import Person


class Manager(Person): # 继承Person类
    def getfirstname(self): # 添加查询lastname的行为
        return self.name.split()[0]


if __name__ == '__main__':
    tom = Manager('Tom Jones', 50, 50000, 'bos')
    bob = Person('Bob Smith ', 45, 30000, 'software')

    print(tom.getfirstname())
    print(tom.getlastname())
    print(bob.getlastname())
    # print(bob.getfirstname())     # 执行报错，bob在Person类中，没有getfirstname方法。
