import pymysql
#创建连接
conn = pymysql.Connect(host="localhost",port=3306,user="wk",passwd="wakewk",db="test01",charset="utf8")
#创建游标
cursor = conn.cursor()
while True:
    # 用户输入信息
    data = input("1.查询所有信息\n2.查询分类信息\n3.只看手机价格\n请输入您要进行的操作ID：")
    if data =='1':
        #1.查询所有信息
        sql = '''select * from goods'''
    elif data=='2':
        #2.查询分组信息
        sql = '''select manu_name,group_concat(name) from goods group by cate_name'''
    elif data=='3':
        #3.只看手机名称及价格
        sql= '''select name,price from goods order by price'''
    elif data=='q':
        break

    cursor.execute(sql)
    datas = cursor.fetchall()
    for temp in datas:
        print(temp)


cursor.close()
conn.close()