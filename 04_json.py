# -*- coding: UTF-8 -*-
import json
dic = {}
dic["name"] = "张二狗"
dic["age"] = 18
dic["height"] = 180
str_json = json.dumps(dic,ensure_ascii=False)
print str_json

dic_obj = json.loads(str_json)
print dic_obj
print dic_obj["age"]