from class_2_person_2_add_action import Person


class Manager(Person): # 继承Person类
    def getfirstname(self): # 添加查询lastname的行为
        return self.name.split()[0]

    def giveraise(self, percent, bonus=0.1): # 修改giveraise方法
        self.pay = int(self.pay * (1.0 + percent + bonus))


if __name__ == '__main__':
    tom = Manager('Tom Jones', 50, 50000, 'bos')
    bob = Person('Bob Smith ', 45, 30000, 'software')

    for obj in [tom, bob]:
        obj.giveraise(0.1)
        print(obj.getlastname(), '=>', obj.pay)
