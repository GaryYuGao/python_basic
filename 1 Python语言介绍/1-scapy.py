import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

ping_one_reply = sr1(IP(dst='88.88.88.2') / ICMP(), timeout=1, verbose=False)
ping_one_reply.show()
