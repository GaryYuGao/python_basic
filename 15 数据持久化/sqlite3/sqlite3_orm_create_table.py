from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


# ----------------sqlite3----------------
engine = create_engine('sqlite:///sqlalchemy_sqlite3.db?check_same_thread=False',
                        # echo=True
                        )
# ----------------mysql----------------
# default（自动选择可用驱动）
# engine = create_engine('mysql://scott:tiger@localhost/foo')
# mysqlclient 驱动
# engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
# PyMySQL 驱动
# engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')
# ----------------psql----------------
# default（自动选择驱动）
# engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')

# psycopg2 驱动
# 安装依赖：yum install postgresql-devel; pip3 install psycopg2-binary
# 修改认证方案
# https://dothanhlong.org/fix-unable-to-connect-to-postgresql-server-scram-authentication-requires-libpq-version-10-or-above/
# 运行./psql/docker_run_script.sh拉起psql
# engine = create_engine('postgresql+psycopg2://qytangdbuser:Cisc0123@192.168.31.148/qytangdb')

# pg8000 驱动
# engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')


Base = orm.declarative_base()

class User(Base):
    __tablename__ = 'users'
    # PSQL的Data Type
    # https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#postgresql-data-types
    id = Column[int](Integer, primary_key=True)
    username = Column[str](String(64), nullable=False, index=True)
    password = Column[str](String(64), nullable=False)
    realname = Column[str](String(64), nullable=True)
    email = Column[str](String(64), nullable=False, index=True)

    def __repr__(self):
        return f"{self.__class__.__name__}(username: {self.username} | email: {self.email})"


if __name__ == '__main__':
    # checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
    Base.metadata.create_all(engine, checkfirst=True)
