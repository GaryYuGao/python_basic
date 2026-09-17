from initdata import db
from datetime import date
import pickle

dbfile = open('peopole-pickle.pl', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

dbfile = open('peopole-pickle-datetime.pl', 'wb')
pickle.dump({'today': date.today()}, dbfile)
dbfile.close()
