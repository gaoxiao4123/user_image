import MySQLdb

db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="123456",
    db="mysql",
    charset="utf8"
)

def first_conn():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()
    print "Database version : %s "% data
    # 关闭数据库连接
    db.close()

#查询
def select():
    cursor = db.cursor()
    sql = "SELECT * FROM china LIMIT 10"
    try:
        cursor.execute(sql)
        #获取整个结果集
        results = cursor.fetchall()
        for row in results:
            print str(row[0]) + "|" + row[1] + "|" + str(row[2])

    except Exception,e:
        print e
        db.close()

#插入
def insert():
    cursor = db.cursor()
    sql = "INSERT INTO CHINA(ID,NAME,PID) VALUES(-1,'test',0)"
    try:
        cursor.execute(sql)
        # 提交事务
        db.commit()

    except Exception, e:
        print e
        # 回滚事务
        db.rollback()
        db.close()

#更新
def update():
    cursor = db.cursor()
    sql = "UPDATE CHINA SET NAME = 'UPDATE' WHERE NAME = 'test'"
    try:
        cursor.execute(sql)
        # 提交事务
        db.commit()

    except Exception, e:
        print e
        # 回滚事务
        db.rollback()
        db.close()

#删除
def delete():
    cursor = db.cursor()
    sql = "DELETE FROM CHINA WHERE NAME = 'UPDATE'"
    try:
        cursor.execute(sql)
        # 提交事务
        db.commit()

    except Exception, e:
        print e
        # 回滚事务
        db.rollback()
        db.close()


if __name__ == '__main__':
    pass
    #first_conn()
    #select()
    #insert()
    #update()
    #delete()

def abc(c,a=1,b=2):
    c = a+b;
    print c

