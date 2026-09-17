import xmltodict
from pprint import pprint
import json
from xml.dom import minidom


xml_file = open('xml_1_xml.xml', 'r').read()  # 打开分析的XML文件

xmldict = xmltodict.parse(xml_file, encoding='utf-8') # 读取xml并转换到OrderedDict字典[有序字典]
pprint(xmldict)

# ----------------提取部分完整信息----------------
pprint(xmldict['root']['公司']['部门'])
depart_list = []

for depart in xmldict['root']['公司']['部门']:
    depart_dict = {'depart_name': depart['@name'],
                   'teacher_list': [t['@name'] for t in depart['师资']['老师']],
                   'course_list': [c['@name'] for c in depart['课程']['课程名']]
                   }
    depart_list.append(depart_dict)

pprint(depart_list)

# ----------------修改----------------
xmldict['root']['公司']['部门'][1]['@name'] = '乾颐堂安全'  # 修改内容

# ----------------写回到XML----------------
with open('xml_1_xmltodict.xml', 'w', encoding='utf-8') as x:
    x.write(minidom.parseString(xmltodict.unparse(xmldict)).toprettyxml(indent='  '))
