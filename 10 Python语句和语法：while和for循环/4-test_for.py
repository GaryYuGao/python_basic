List1 = ['aaa', 111, (4, 5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4, 5)]
for x in List1:
    for y in List2:
        if x == y:
            print(str(x), 'in List1 and List2')
            break
    else:
        print(str(x), 'only in List1')
