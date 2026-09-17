import shelve
from datetime import timedelta

db = shelve.open('people-shelve')
cq_bomb = db['cq_bomb']  # 读取数据库键'cq_bomb'中的字典
cq_bomb['pay'] *= 1.6  # 更新字典
db['cq_bomb'] = cq_bomb  # 把更新后的字典重新写回数据库键
db.close()


db = shelve.open('people-shelve')
datetime_now = db['datetime']  # 读取数据库键'cq_bomb'中的字典
datetime_now += timedelta(days=4)  # 更新字典
db['datetime'] = datetime_now  # 把更新后的字典重新写回数据库键
db.close()


db = shelve.open('people-shelve')
print(db['datetime'])
db.close()