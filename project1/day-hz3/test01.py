import pymysql
#创建连接
conn = pymysql.connect(host="localhost",port=3306,user="wk",passwd="wakewk",db="test01",charset="utf8")
#创建游标
cursor = conn.cursor()
for i in range(100000):
    sql = "insert into test_index (content) values ('ha-%d')"%i
    cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()