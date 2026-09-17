from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import User, engine


# 1. 创建会话工厂（绑定数据库引擎，全局只需要创建一次）
Session = sessionmaker(bind=engine)

# 2. 生成一个会话实例
session = Session()

# 插入一个条目数据
user1 = User(username='qinke',
            password='cisco',
            email='collinsctk@qytang.com')
session.add(user1)
session.commit()

user2 = User(username='tina',
            password='cisco',
            realname='qyttina',
            email='tina@qytang.com')
session.add(user2)
session.commit()

user3 = User(username='ender',
            password='cisco',
            realname='周亚军',
            email='ender@qytang.com')
session.add(user3)
session.commit()

# 一次性插入多个条目
# session.add_all([new_user, user2])
# session.commit()

# 用完关闭会话
session.close()
