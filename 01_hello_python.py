#coding=utf-8
intt = 10
print intt

print abs(-100)
# 比较大小 左边大返回1 相等返回0  右边大返回-1
print cmp(1,2)

tuple01= (1,2,3,4,5,"a","b",123L,1.01)
tuple02= (1,2,3,4,5,"a",1.01)
print tuple01[1:5]
#for x in tuple01:
#    print x
print cmp(tuple01,tuple02)

dict1 = {'gaga':123,(1,2,3): "aaa",1:'a'}
dict2 = {'gaga':123,(1,2,3): "aaa"}
dict["new"] = 999
print cmp(dict1,dict2)


