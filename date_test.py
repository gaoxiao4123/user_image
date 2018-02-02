# -*- coding: UTF-8 -*-
import datetime
now = datetime.datetime.now()
print now
print now.strftime('%Y-%m-%d %H:%M:%S')

t_str1 = '2015-04-07 19:11:21'
t_str2 = '2005-03-08 19:11:21'
d1 = datetime.datetime.strptime(t_str1,'%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(t_str2,'%Y-%m-%d %H:%M:%S')
print (d1 - d2)

year = datetime.timedelta(days=365,seconds=1000)
ten_years = year * 10
nine_years = ten_years - year
print "一年",year
print "十年",ten_years
print "九年",nine_years