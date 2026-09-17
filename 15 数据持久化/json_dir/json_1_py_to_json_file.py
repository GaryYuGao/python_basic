import json
from source_db import qyt_teachers, qyt_courses #导入字典

# 写入
print('把Python对象转换为JSON格式，并且写入文件')
with open('./json_0_qyt_teachers.json', 'w', encoding='utf-8') as f:
    json.dump(qyt_teachers, f, ensure_ascii=False, indent="    ")

with open('./json_0_qyt_courses.json', 'w', encoding='utf-8') as f:
    json.dump(qyt_courses, f, ensure_ascii=False, indent="    ")

with open('./json_0_true.json', 'w', encoding='utf-8') as f:
    json.dump({"qytang": True}, f, ensure_ascii=False)

# 读取
with open('./json_0_qyt_teachers.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
    print(new_dict)
