import pickle

dbfile = open('peopole-pickle.pl', 'rb')
db = pickle.load(dbfile)
dbfile.close()

print(db)

db['cq_bomb']['pay'] *= 1.6  # 提高工资

dbfile = open('peopole-pickle.pl', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
