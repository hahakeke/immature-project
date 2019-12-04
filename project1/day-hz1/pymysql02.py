from pymysql import connect

class JD:
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='wk', passwd='wakewk', db='test01', charset='utf8')
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def execute_option(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        sql = 'select * from goods'
        self.execute_option(sql)

    def show_cates(self):
        sql = 'select cate_name from goods group by cate_name'
        self.execute_option(sql)

    def show_brands(self):
        sql = 'select manu_name from goods group by manu_name'
        self.execute_option(sql)

    def insert_items(self):
        item_name = input("请输入您要插入的数据：")
        sql = """insert into brands (manu_name) values ("%s")"""%item_name
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        search_name = input("请输入你要查找的信息:")
        # sql = """select * from goods where name='%s';"""%search_name    # 这类输入查询易造成SQL注入
        # print('---------->%s<-----------'%sql)
        # self.execute_option(sql)
        sql = "select * from goods where name=%s"  #  调用execute函数减小注入的几率
        self.cursor.execute(sql,[search_name])
        print(self.cursor.fetchall())
    @staticmethod
    def show_describe():
        print("----------1.查询所有信息---------")
        print("----------2.查询类别-------------")
        print("----------3.查询商品类别---------")
        print("----------4.插入数据---------")
        print("----------5.查询需要的信息---------")
        return input("请输入您要进行的操作编码：")

    def run(self):
        while True:
            opt = self.show_describe()
            if opt == "1":
                self.show_all_items()
            elif opt == "2":
                self.show_cates()
            elif opt =="3":
                self.show_brands()
            elif opt == "4":
                self.insert_items()
            elif opt == "5":
                self.get_info_by_name()
def main():
    jd = JD()
    jd.run()
    # 1.查询所有信息
    # 2.查询类别
    # 3.查询商品类别

if __name__ == '__main__':
    main()