import json

# 此时student 是一个dict格式内容，不是json
student={
    "name": "ljb",
    "age": 37,
    "mobile": "1801551111"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("json对象:{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)