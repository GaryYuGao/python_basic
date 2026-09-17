from module1.l1 import l1_abc_add, l1_username, l1_password
from module1 import abc_add, username, password
from module1.l2.l2 import l2_abc_add, l2_username, l2_password

print(abc_add(username, password))
print(l1_abc_add(l1_username, l1_password))
print(l2_abc_add(l2_username, l2_password))
