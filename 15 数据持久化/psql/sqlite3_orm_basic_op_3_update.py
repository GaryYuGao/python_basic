from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import User, engine

# 创建会话工厂并绑定数据库引擎
Session = sessionmaker(bind=engine)
session = Session()

# 更新一个条目：查询用户名以tina开头的用户（仅匹配一条）
user1 = session.query(User).filter(User.username.like('tina%')).one()
print(user1.email)

# 修改为新的值
user1.email = 'tina@gmail.com'
# 提交事务，将修改持久化到数据库
session.commit()
