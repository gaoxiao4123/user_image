#coding=utf-8
try:
    fh = open("testfile","r")
    fh.write("tessttttsstatatatat")
except IOError:
    print "Error: can\'t find file or read data"

class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg

try:
    raise Networkerror("自定义异常")
    print 'sadadadadad'
except Networkerror,e:
    print e.args
    print 'sadadadadad'

strr = raw_input("请输入:");
print "你输入的是", strr