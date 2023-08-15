from xml.etree import ElementTree as ET

# # 1、打开xml文件
# tree =ET.parse(r"./demo.jmx")
# # 获xml文件的内容取根标签
# root = tree.getroot()
# print(root)

# Code_object = root.iter("boolProp")

# print(Code_object)

# for code in Code_object:
#     print(code.tag, code.attrib['name'], code.text)


# def read_jmx(jmx_path, tag, name) -> str:
#     """read jmx"""
#     tree =ET.parse(jmx_path)
#     root = tree.getroot()
#     tag_object = root.iter(tag)
#     for tag_target in tag_object:
#         if tag_target.attrib['name'] == name:
#             return tag_target.text
#     raise Exception('no tagname found')

# def write_jmx(jmx_path, tag, name, text) -> str:
#     """read jmx"""
#     tree =ET.parse(jmx_path)
#     root = tree.getroot()
#     tag_object = root.iter(tag)
#     for tag_target in tag_object:
#         if tag_target.attrib['name'] == name:
#             tag_target.text = text
#             tree.write(jmx_path, encoding='utf-8')
#             return True
#     return False


# print(read_jmx('./demo.jmx', 'boolProp','TestPlan.functional_mode'))

# write_jmx('./demo.jmx', 'boolProp','TestPlan.functional_mode', 'false')
import socket

print(socket.gethostname())